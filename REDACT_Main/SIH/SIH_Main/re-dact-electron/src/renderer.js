const { ipcRenderer } = require('electron');

document.getElementById('chooseFileButton').addEventListener('click', () => {
  ipcRenderer.send('open-file-dialog');
});

ipcRenderer.on('selected-file', (event, filePath) => {
  document.getElementById('fileInput').value = filePath;
});

document.getElementById('redactButton').addEventListener('click', () => {
  const filePath = document.getElementById('fileInput').value;
  const redactionLevel = document.getElementById('redactionLevel').value;
  const redactionStyle = document.querySelector('input[name="redactionStyle"]:checked').value;
  const redactionMode = document.querySelector('input[name="redactionMode"]:checked').value;

  console.log('Redact button clicked');
  console.log('File:', filePath);
  console.log('Redaction Level:', redactionLevel);
  console.log('Redaction Style:', redactionStyle);
  console.log('Redaction Mode:', redactionMode);

  // Implement the redaction logic here
});
