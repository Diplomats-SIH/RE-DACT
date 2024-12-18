// preload.js
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    runPythonScript: (arg) => ipcRenderer.invoke('run-python-script', arg)
});
