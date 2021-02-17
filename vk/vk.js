//'VK authentication constants
var ClientId = "read from storage";

var RedirectUri = "https://oauth.vk.com/blank.html";
var AuthUri = "https://oauth.vk.com/authorize?client_id=" + ClientId + "&redirect_uri=" + 
		RedirectUri + "&response_type=token&scope=wall,docs";

var uploadUrl;

function VKMethod(method, args) {
	
	var addr = "https://api.vk.com/method/" + method + "?v=5.101&access_token=" + GetAccessToken() + "&" +args;
				  
	var resp = JSON.parse(httpGet(addr));
   	
	if ("response" in resp) return resp.response;
    
    var errcode = resp.error.error_code;
     	
   	switch(errcode)
   	{
   		case 5:
   			//W.Echo "Authentication code needs to be updated"
  
   			var at=RenewAccessToken();
   			if (typeof at!="undefined")
   				return VKMethod(method, args);
   			else {
   				throw "Без доступа к методам программа ничего не может совершить.";
   				return;
   			}
   			
   		case 14:	//captcha 			
 			captcha_img = resp.error.captcha_img;
 			captcha_sid = resp.error.captcha_sid;
 			
   			wShell.Run (captcha_img);
   			captcha_key = prompt("Captcha requested.");
   			
   			if (captcha_key==null) throw("Cannot proceed without captcha.");
   			
   			args = args + "&captcha_key=" +captcha_key+ "&captcha_sid="+captcha_sid;
   			return VKMethod(method, args);
   			
   		default:
   			echo("VKMethod",method,"error",errcode); 
   			return resp.error;			
 	}
 	
}

/*
Function GetAccessToken()
	If len(accessToken)=0 Then
		accessToken = RenewAccessToken()
		SaveSetting "accessToken", ,accessToken 
	End If
	
	GetAccessToken = accessToken
End Function

Function RenewAccessToken

	'navigate browser to AuthUri
	wShell.Run AuthUri
		
	accessToken = InputBox("Введите access token (тоукен доступа)")
	if len(accessToken)	then SaveSetting "accessToken", ,accessToken
		
	RenewAccessToken = accessToken

End Function


Function GetAccessToken()
	
	If fso.FileExists(accessTokenFile) Then
		Set atFileStream = fso.GetFile(accessTokenFile).OpenAsTextStream(ForReading)
		If Not atFileStream.AtEndOfStream then
			accessToken = atFileStream.ReadLine()
			
		End if
	End If
	
	If IsEmpty(accessToken) Then
		accessToken = RenewAccessToken()
	End If
	
	GetAccessToken = accessToken
End Function

Function RenewAccessToken

	StartIE
	ie.navigate AuthUri
	While ie.Busy And ie.ReadyState<>READYSTATE_COMPLETE:Wend
	
	locationURL = ie.LocationURL
		
	'w.Echo accessToken
	accessToken = GetUrlParameter(locationURL, "access_token")
	
	If IsNull(accessToken) Then
		ie.visible = True
		self.close
		Do:loop
	End If
	
	'FreeIE	
	
	fso.OpenTextFile(accessTokenFile, ForWriting, True).WriteLine(accessToken)

End Function
*/