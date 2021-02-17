'
'Gloria in excelsis Deo.
'


'=================
'= HTTP get/post
'=================
Function httpPostXmlAsync (addr, requestBody, onReadyStateChange)

	With xmlhttp
     	.open "POST", addr, True
     	
    	If Len(userAgent) Then .setRequestHeader "User-Agent", userAgent
    	
    	.setRequestHeader "Content-Type", "application/x-www-form-urlencoded"
    	
    	SendCookies addr
			    	
       	.onreadystatechange = onReadyStateChange
       	
   		On Error Resume Next
   		httpPostXmlAsync = .send ( requestBody )
		CheckHttpErrorsAndSetCookies addr
		
    End With
End Function

function httpPostXml (addr, requestBody)

    With xmlhttp
     	.open "POST", addr, False
		If Len(userAgent) Then .setRequestHeader "User-Agent", userAgent
    	
        .setRequestHeader "Content-Type", "application/x-www-form-urlencoded"
        	
    	.onreadystatechange=nothing
       	SendCookies addr
			    	
		On Error Resume Next
    	.send requestBody
    	CheckHttpErrorsAndSetCookies addr
      	
    	If Err=0 Then Set httpPostXml = .responseXML else set httpPostXml=nothing
    
    End With
end Function

function httpPost (addr, requestBody)
    With xmlhttp
     	.open "POST", addr, False
		If Len(userAgent) Then .setRequestHeader "User-Agent", userAgent
    	
        .setRequestHeader "Content-Type", "application/x-www-form-urlencoded"
        	
    	.onreadystatechange=nothing
       	SendCookies addr
			    	
		On Error Resume Next
    	.send requestBody
    	CheckHttpErrorsAndSetCookies addr
      	
      	alert .responseText
    	If Err=0 Then httpPost = .responseText else httpPost=""
    
    End With
end Function

function httpGetXml (addr)

    With xmlhttp
    	.open "GET", addr, False
    	If Len(userAgent) Then .setRequestHeader "User-Agent", userAgent
    		
    	.onreadystatechange=nothing
    	SendCookies addr
	 	
	 	On Error Resume Next
    	.send    	
   		CheckHttpErrorsAndSetCookies addr
    	If Err=0 Then Set httpGetXml = .responseXML else set httpGetXml=nothing
    
    End With
end Function

'Function httpGet (addr)

'	With xmlhttp
'		.open "GET", addr, False
'	
'		If Len(userAgent) Then .setRequestHeader "User-Agent", userAgent	
'		
'    	.onreadystatechange=nothing
'	 	SendCookies addr
'		
'		On Error Resume next
'		.send
'		CheckHttpErrorsAndSetCookies addr
'		If Err=0 Then
'			httpGet = .responseText
'		Else
'			MsgBox "httpGetXml error." & vbLf & addr & vbLf & Err.Description
'			httpGet=""
'		End If
'		
'	End With
'End Function

Function httpGetAsync(addr, handler)

	With xmlhttp
    	.open "GET", addr, True
    	.onreadystatechange = handler
    	If Len(userAgent) Then .setRequestHeader "User-Agent", userAgent
    	
    	SendCookies addr
    	
    	On Error Resume Next
    	httpGetAsync = .send
   
    	CheckHttpErrorsAndSetCookies addr
    	
    End With
   
End Function

Function SendCookies(addr)
'	Dim cookies

	domain=htmla(addr).hostname
	path=htmla(addr).pathname

	reqCookies=GetCookies(domain, path)

	If Len(reqCookies) Then	'for this address, obviously
   		xmlhttp.setRequestHeader "Cookie", reqCookies
	End If
		
End Function



Function CheckHttpErrorsAndSetCookies(addr)
	If Err Then
		alert format("Ошибка при соединении с интернетом: ", Err.Description, _
					vbLf, Hex(Err.Number))
	Else
		domain=htmla(addr).hostname
		path=htmla(addr).pathname
		If xmlhttp.readyState=READYSTATE_COMPLETE Then SetCookies xmlhttp.getAllResponseHeaders, domain, path
	End If
	
End function



'=================================================
'= Upload
'=================================================

'Build multipart/form-data document with file contents And header info
Function BuildFormData(content)
	Dim Pre, Po
	Const ContentType = "application/octet-stream"	
	
	Set file=content("file")
	fileContents=ReadFile(file)
	if IsNull(fileContents) then
		BuildFormData=null
		exit function
	end if
		
	'The two parts around file contents In the multipart-form data.
	
	'Build source form with file contents
	d = "--" + MPFDBoundary + vbCrLf
	
	For Each param In content
		If Not(IsObject(content(param))) then
			d = d + "Content-Disposition: form-data; name=""" & param & """" & vbCrLf & vbCrLf
			d = d + content(param) + vbCrLf + "--" + MPFDBoundary + vbCrLf
		End If
	Next
	
	fileName = fso.GetFileName(file.path)
	d = d + "Content-Disposition: form-data; name=""file""; filename=""" & fileName &  """" +vbcrlf
	d = d + "Content-Type: " + ContentType + vbCrLf + vbCrLf
	'd=d+"Content-Length: " +  + vbCrLf + vbCrLf
	
	Pre = d
	Po=vbCrLf + "--" + MPFDBoundary + "--" & vbCrLf
	
	'Build form data using streams.

	Set stream2 = CreateObject("adodb.stream")
	stream2.Open
	stream2.Type= adTypeBinary
	
	With oStream
		.Open
		.Type = adTypeText
		.Charset = "utf-8"
		.WriteText Pre
		.Position=3
		.CopyTo stream2
				
		stream2.Write fileContents
		
		.Position=0
		.WriteText Po
		.SetEOS
		.Position=3
		.CopyTo stream2
	
		.position=0
		.seteos
		.Close
	End With
	
	stream2.Position=0
	BuildFormData = stream2.Read
	
	stream2.Position=0	
	stream2.SetEOS
	stream2.Close
	
	Set stream2=nothing
	
End Function


'====================================================================
'Other http functions.
'========================================

'Parse URL, get parameter from an url
'Needs to be rewritten to use built-in VB capabilities (or Javascript)
'
Function GetURLParameter(URL, Parameter)

	instrUrlParameter = InStr(URL, Parameter & "=")
	If instrUrlParameter = 0 Then
		GetURLParameter = Null
		Exit function
	End if

	URLParameter = Mid(URL, instrUrlParameter)
	ampersandPosition = InStr(urlparameter, "&")
	If ampersandPosition Then
		urlparameter = Left(urlparameter, ampersandposition - 1)
	End If
	urlparameter = Mid(urlparameter, InStr(urlparameter, "=")+1)
	GetURLParameter = Trim(urlparameter)
	'WScript.Echo "Parsing URL " & url & ", found parameter " & urlparameter	
End Function


Set xmlHttp = CreateObject("MSXML2.ServerXMLHTTP.6.0")

With xmlHttp
	.setTimeouts 0,0,0,0
	.setOption SXH_OPTION_IGNORE_SERVER_SSL_CERT_ERROR_FLAGS, SXH_SERVER_CERT_IGNORE_ALL_SERVER_ERRORS

	'.setOption SXH_OPTION_ESCAPE_PERCENT_IN_URL, True
End With

'==========================================================================
'=
'= Cookie functions.
'=


Set cookies=CreateObject("adodb.recordset")
	
If fso.FileExists(cookiesFile) Then
	cookies.Open cookiesFile
Else
	cookies.Fields.Append "name", adVarChar, 40
	cookies.Fields.Append "value", adVarChar, 500
	cookies.Fields.Append "domain", adVarChar, 40
	cookies.Fields.Append "path", adVarChar, 100
	cookies.Fields.Append "expires", adVarChar, 40
	cookies.Open
End If


Function SetCookies (responseHeaders, urlDomain, urlPath)
	
	Set newCookies = regexmatches(responseHeaders, "Set-Cookie:.+(\n|$)")
	
'	echo "SetCookies entry. Is object cookies?", IsObject(cookies)
	
	For Each match In newCookies	
		cookie=match.value
		
		name = regexsubmatch(cookie, " ([^=]+)=")
		value = regexsubmatch(cookie, "=([^;]+);")
		path = regexsubmatch(cookie, "path=([^;]+)")
		domain = regexsubmatch(cookie, "domain=([^;]+)")
		expires = regexsubmatch(cookie, "expires=([^;]+)")
		
		If domain="" Then domain=urlDomain
		If path="" Then path=urlPath		
	
		'if expires set to past date, delete the cookie.

		If cookies.BOF Then	
			cookies.AddNew
		Else
			cookies.MoveFirst
			cookies.find "name='" & name & "'"
			If cookies.EOF Then
				cookies.AddNew
			End if
		End If
			
		cookies.update Array("name", "value", "domain", "path", "expires"), _
						Array(name, value, domain, path, expires)

	next
	 
	'сохранить cookie и token.
	cookies.save cookiesFile, adPersistXML

End Function

Function GetCookies(domain, path)
	
	If cookies.BOF Then GetCookies="": Exit Function
	
	cookies.MoveFirst
	While Not(cookies.EOF)
		expires=cookies.Fields("expires")
		If getDate(expires).valueOf()<getDate().valueOf() Then
			'cookie date expired.
			cookies.Delete
			cookies.Update
			updated=true
		End If
		
		ckDomain=cookies.Fields("domain")
		ckPath=cookies.Fields("path")
		
		'echo "Domain:", domain, "ckDomain:", ckDomain, _
		'	"Path:", path, "ckPath:",  ckPath
		
		If instr(domain, ckDomain)>0 And InStr(path, ckPath)>0 Then
			'echo "adding cookie"
			cookiesStr=cookiesStr & cookies.Fields("name")& "=" & cookies.Fields("value")& "; " 
		End If
			
		cookies.MoveNext
	Wend
	
	If updated Then
		cookies.Save cookiesFile, adPeristXML
	End If
	
	GetCookies=cookiesStr
End Function

Function CleanCookies()
	If cookies.BOF Then Exit Function
	cookies.MoveFirst
	While Not(cookies.EOF)
		expires=cookies.Fields("expires")
		If expires="" Or getDate(expires).valueOf()<getDate().valueOf() Then
			'session cookie, delete.
			cookies.Delete
			cookies.Update
		End if
			
		cookies.MoveNext
	Wend
	cookies.Save cookiesFile, adPersistXML
End function

