'
' Gloria in excelsis Dei, et in terra pax, hominibus bonae voluntatis.
'

'Returns file contents As a binary data
Function ReadFile(File)
	Dim Stream: Set Stream = CreateObject("ADODB.Stream")
	Stream.Type = 1 'Binary
	Stream.Open

	on error resume next
	Stream.LoadFromFile File.Path
	if err then
		echo "Reading file error:", File.Path, vblf, err.Description
		ReadFile=null
	else
		ReadFile = Stream.Read	
	end if
	on error goto 0
	
	'WScript.Echo Stream.read
	Stream.Close
	Set Stream=nothing
End Function

'utf-8 write
'Sub WriteFile(file)

'	Set inStream=WScript.CreateObject("ADODB.Stream")
'	Set outStream=WScript.CreateObject("ADODB.Stream")
							
'	inStream.Open
'	inStream.type=adTypeBinary
'	inStream.LoadFromFile(file)
'	inStream.Position=3
	
'	outStream.Open
'	outStream.type=adTypeBinary
'	outStream.Write instream.Read
	
'	inStream.Close()
'	outStream.SaveToFile file, adSaveCreateOverWrite						
			
'	outstream.Close
'End sub	

'

Function dump(var)
	Set table=newtable
	For Each key In var
		table.appendChild NewTR(Array(key, var(key)))
	Next
	document.body.insertbefore table,tabs
End Function

'======

Function newdict()
	Set newdict = CreateObject("scripting.dictionary")
End Function


If Len(settingsFile)=0 Then
	Const settingsFile="./settings.inc"
ElseIf Not(fso.FileExists(settingsFile)) Then
	call fso.CreateTextFile (settingsFile,, True)
End if

Function SaveSetting(name, key, value)
	Dim settings, nokey	'to ensure there isn't a global of this name
		
	'find and replace or append
			
	On Error Resume Next
	a=(key="")
	If Err or key="" Then nokey=True
	On Error Goto 0
		
	If nokey Then
		setting=name & "="
		settingPattern = "(" & name & "="").*"""
			
		'also assign the variable immediately:
		statement= format(name, "=""", value, """")	
	Else	
		setting=name & "(""" & key & """)="
		settingPattern = "(" & name & "\(""" & key & """\)="").*"""
		decl = format("Set ", name, "=newdict")
		
		'also assign the variable immediately:
		If IsObject(Eval(name))=0 Then
			'declaration not found, declare the variable now.
			ExecuteGlobal decl
		End if
		statement= format(name, "(""", key, """)=""", value, """")
	End If
	ExecuteGlobal statement
	
	Set oSF=fso.OpenTextFile(settingsFile, ForReading,, TristateTrue)
	If oSF.AtEndOfStream=False Then settings=oSF.ReadAll
	osf.Close
	
	If InStr(settings, setting) Then
		settings=regexreplace(settings, settingPattern, "$1" & value & """")
	Else
		settings = settings & setting & """" & value & """" & vbCrLf
	End If
	
	If Len(decl) and InStr(settings, decl)=0 Then
		declPattern=format("(Set .+=newdict[\S\s]+Set .+=newdict)\s")
		settings=decl & vbLf & settings
	End If
		
	set oSF=fso.OpenTextFile(settingsFile, ForWriting,, TristateTrue)
	oSF.Write settings
	oSF.Close
	
End Function

'=================================================
'Checks if there is a connected network adapter.
'=================================================
Function CheckInternet()
	Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")
	Set colItems = objWMIService.ExecQuery("Select * from Win32_NetworkAdapter",,48)
	For Each objItem in colItems
   		If objItem.NetConnectionStatus=2 Then
   			CheckInternet=True
   			Exit function
   		End If
    Next
    CheckInternet=False
End function


function AllowClickingWords (elementsArray)
	Const onDblClickCommand = "Clickable_OnDblClick(window.getSelection())"
	
	If IsArray(elementsArray) then
		For Each el In elementsArray
		'	el.attributes.onclick.value="Clickable_OnClick()"
			el.attributes.ondblclick.value=onDblClickCommand
		Next
	Else
		elementsArray.attributes.ondblclick.value=onDblClickCommand
	End If
end Function


Function GetAccessToHtml(div)

'	echo "GATH ", div.id
	If Not(IsObject(div)) Then Set div=document.getElementById(div)
	For Each child In div.children
		'If instr(child.id, "_") Then
		If Len(child.className) then
			'statement=Join(array("set", regexsubmatch(child.id, "^(.+)_"), _
		'						"=document.GetElementByID(""" & child.id & """)"))
			statement=format("set ", child.className, "=child") '_
								'"=document.GetElementByID(""" & child.id & """)")
		'	echo statement
			ExecuteGlobal format("dim ", child.className)
			Execute statement
		End If
	Next
End function

Randomize

Class Tabs
	'Wishlist: write the same in Javascript for easier access. 
	'write another class for tab.
	
	Private tabsHolder, divTabLinks, divTabs, tabLinks
		
	Public Property Set Container(element)
		Set divTabLinks=CreateHtmlElement("div", "class", "divTabLinks")
		Set divTabs=CreateHtmlElement("div", "class", "divTabs")
		divTabLinks.style.display="block"
		divTabs.style.display="block"	
		
		Set tabsHolder=element
		With tabsHolder
			.appendChild divTabLinks
			.appendChild divTabs
		End With
		Set tabLinks=newdict
	End Property
	
	Public Function AddTab(title, divTab, id)
		
		if IsObject(divTab) then
			'clone the div element to get a new independent tab.
			Set divTab=divTab.cloneNode(true)
		else
			Set divTab= CreateHTMLElement("div")
		end if
		
		divTab.style.display="none"
		divTab.style.height="100%"
		
		if id="" then id="divTab" & regexreplace(CStr(Rnd()), "[,-\.]", "")
		divTab.id=id
		
		divTabs.appendChild divTab
		If divTabs.children.length=1 Then
			divTab.style.display="block"
		End If
				
		'create the link that will be the visible tab.
		Set aDivTab=createHtmlElement("a", "onclick", "TabLink_OnClick(" & id & ")", title)
	
		divTabLinks.appendChild aDivTab
		
		Set tabLinks(id)=aDivTab
		
		SwitchTo divTab
		Set AddTab=divTab
	End Function
	
	Public Function GetTab(tabId)
		If IsNull(document.getElementById(tabId)) then
			Set GetTab=nothing
		Else
			Set GetTab=document.getElementById(tabId)		
		End if
	End Function
	
	Public Function SwitchTo(tabTarget)
		'todo: accept both id and div itself
		TabLink_OnClick tabTarget
	End Function
	
	Public Function ShiftTab(tab)
		Set tabLink=tabLinks(tab.id)
			On Error Resume next
		tabLink.NextSibling.insertAdjacentElement "afterend", tabLink
	'	divTabLinks.removeChild tabLink
	End Function
	
	Public Function CloseTab(tab)
		If Not(isobject(tab)) Then Set tab=document.getelementbyid(tab)
		
		on error resume next
		set switchTarget=tab.NextSibling
		on error goto 0
		
		divTabs.removeChild tab
		divTabLinks.removechild tabLinks(tab.id)
		
		Set tab=Nothing
		
		if not(isobject(switchTarget)) then set switchTarget=divTabs.firstChild
		SwitchTo switchTarget
		
	End function
	
	public function SetTitle(tab, title)
		tabLinks(tab.id).innerHTML=title
	end function
	
End Class

Function TabLink_OnClick(tabSwitchTo)
	
	Set elem=tabSwitchTo.parentElement
	
	If IsObject(divTab) Then
		alert "The tab mechanism requires the name divTab to be free, but it is already taken." & vbLf & _
				"Now the error is going to fire."
	End If
	
	For Each divTab In tabSwitchTo.parentElement.children
	'	alert "hiding " & divtab.outerhtml
		divTab.style.display="none"
	Next
	tabSwitchTo.style.display="block"
	
End Function

' returns Tabs
Function GetTabs(elem)
End Function

'====================================================================

'================================================================================
SetLocale("ru-ru")

'wshell


'
'= So weird :) 
' How to otherwise get the path of a Shell folder object?
'
Function FolderPath(shFolder)
	FolderPath = shfolder.ParentFolder.ParseName(shFolder.title).Path
End Function


'Includes another script.
'Sub Include(file)
'	Set fso=CreateObject("scripting.filesystemobject")
'		
'	If fso.GetDriveName(file)="" Then
'		file = fso.BuildPath(scriptPath, file)
'	End if

'	If fso.GetFileName(file)="adovbs.inc" Then
'		UnicodeState=TristateFalse
'	Else	
'		UnicodeState=TristateTrue
'	End If

	'alert file
'	On Error Resume Next
'	code = fso.OpenTextFile(file,,, UnicodeState).ReadAll()
'	If Err Then
'		call msgbox format("Include file ", file, " error.", vbLf, Err.Description)
'	End If
'	
'	If fso.GetFileName(file)<>"strings.vbs" Then
'		code=RegExReplace(code, "^<%|%>$", "")
'	End If
'	
'	ExecuteGlobal (code)
'End Sub



'====================================

