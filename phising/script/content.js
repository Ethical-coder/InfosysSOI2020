//this function  will be used to send alert or noticifications after recieving response back from python
function finalAction(data){
	var output=data.result;
	alert(data.message);
};


//function for sending api request to flask server
function api_post(url,type){
    var xmlHttp=new XMLHttpRequest();
    data=JSON.stringify({"url":url});
    xmlHttp.open("POST","http://127.0.0.1:80/"+type,true);
    xmlHttp.onload=function(){
    	finalAction(JSON.parse(xmlHttp.response));
    };
    xmlHttp.send(data);

};

//get request for getting html of the page
function api_get(link){
	var xmlHttp=new XMLHttpRequest();
	xmlHttp.open("GET",link,false);
	xmlHttp.send(null);
	return(xmlHttp.responseText);

};

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
  	if(request.message=='clicked'){
  		api_post(window.location.toString(),"popup");
      //console.log(api_post("hello from javascript",""));
  	};
  });

function check_beef(link){
	//checking page html for any type of hook
	html_data=api_get(link);
	html_data=html_data.toLowerCase();
	let match_result=html_data.match(/(?:http:\/\/)(.*)(?:::3000\/hook.js)/);
	if(match_result){
		alert("This website is using a hook with ip: :"+result[1]);
	}
	else if(!link.includes("https://")){	
		api_post(link,"content");
	};

};


let link=window.location.toString();
check_beef(link);
