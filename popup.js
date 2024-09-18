document.getElementById('start').addEventListener('click', function() {
  fetch('http://localhost:5000/start')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
});

document.getElementById('stop').addEventListener('click', function() {
  fetch('http://localhost:5000/stop')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
});
