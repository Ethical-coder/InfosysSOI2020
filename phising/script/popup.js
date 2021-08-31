function send_message(message){
	chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, {"message": message});
  });
};





document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById("event triggerer");
    var inject=document.getElementById("inject");
    
    // onClick's logic below:
    link.addEventListener('click', function() {
 	inject.innerHTML=("<h3>Checking The Page...</h3>");
	var message="clicked";
	send_message(message);
    });
});
