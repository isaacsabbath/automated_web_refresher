chrome.runtime.onInstalled.addListener(function() {
  console.log("Extension Installed");
});

chrome.browserAction.onClicked.addListener(function(tab) {
  fetch('http://localhost:5000/refresh')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
});
