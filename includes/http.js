/*
All for the glory of God...
*/


var    READYSTATE_UNINITIALIZED = 0
var    READYSTATE_LOADING = 1
var	READYSTATE_LOADED = 2
var    READYSTATE_INTERACTIVE = 3
var    READYSTATE_COMPLETE = 4


var SXH_OPTION_IGNORE_SERVER_SSL_CERT_ERROR_FLAGS = 2
var SXH_SERVER_CERT_IGNORE_ALL_SERVER_ERRORS = 13056
var SXH_OPTION_ESCAPE_PERCENT_IN_URL = 1
var SXH_OPTION_URL_CODEPAGE = 0

var cookiesFile = "./cookies.xml"

var MPFDBoundary  = "|PtoxosKaiPenes7499|"

function HttpGet (addr, asyncHandler)
{
	try{
		
		xmlhttp.open ("GET", addr, false)
	
		if (typeof userAgent!=='undefined') xmlhttp.setRequestHeader ("User-Agent", userAgent)	
		
		if(typeof asyncHandler!=='undefined')
		{
		}else
		//	xmlhttp.onreadystatechange=null
	 	
	 	if (typeof SendCookies!=='undefined') SendCookies(addr)
		
		xmlhttp.send()
				
	}catch(err){
		return err;
	}	
	
	//set cookies
	domain=htmla(addr).hostname
	path=htmla(addr).pathname
	//if (xmlhttp.readyState==READYSTATE_COMPLETE)
		if (typeof SetCookies!=='undefined')
			SetCookies (xmlhttp.getAllResponseHeaders, domain, path);

	return xmlhttp.responseText
	
}

function HttpGetJSON(addr)
{
	var resp=HttpGet(addr);
	if (typeof resp=="string")
		try{
			return JSON.parse(resp);
		}catch(err){
			return err
		}
	else return resp;
}

function HttpGetAsync(addr, asyncHandler)
{
	return HttpGet(addr, asyncHandler);
}



function DownloadFile(url, location)
{
	var cmdline='powershell -command "& { (New-Object Net.WebClient).DownloadFile(\'' + url + '\', \'' + location + '\') }"';
	wShell.Run(cmdline, 0, true);
}




/*
'=
'= Download
'=
Dim dlQueue, expectingDlLoc, downloading
downloading=False

Function DownloadFile(url, downloadLoc)
	
	With xmlHttp
		If downloading=true Then

			If IsEmpty(dlQueue) then
				Set dlQueue = CreateObject("adodb.recordset")
				With dlQueue
					.Fields.Append "url", adVarWChar, 1000
					.Fields.append "loc", adVarWChar, 1000
					.Open
				End With
			End If
			With dlQueue
				.AddNew Array("url", "loc"), Array(url, downloadLoc)
			 	.Update
			End With
			
		Else	
			.open "GET", url, True	
			If Len(userAgent) then .setRequestHeader "User-Agent", userAgent
			.onreadystatechange = GetRef("xmlhttp_OnReadyStateChange_Download")
			expectingDlLoc=downloadLoc
			downloading=True
			result=.send
			echo "Expecting...", downloadLoc, url, "send result:", result
					
		End If
	End With

	
End Function

'=
'= OnReadyStateChange for download.
'=
Function xmlhttp_OnReadyStateChange_Download()
	
	With xmlhttp
		If .readyState <> READYSTATE_COMPLETE Then Exit Function
							
		contentType = .getResponseHeader ("Content-Type")
		If InStr(contentType, "text/html") Then	
			'was it meant to download html? maybe vk returns some html instead of the file?
		End If
		
		If .Status = 200 And Len(.responseBody) Then
				
			With oStream
				.Open
				.Type = adTypeBinary    
				.Write xmlHttp.responseBody
				
				.SaveToFile expectingDlLoc, adSaveCreateOverWrite
				.Close
			End With
			echo "Received", expectingDlLoc			
		
		End If
	End With
	
	downloading=False
	
	With dlQueue

		If .RecordCount Then
			.MoveFirst
			url=.Fields("url")
			loc=.Fields("loc")
			.Delete
		
			DownloadFile url, loc
		End If
	End With
End function
*/