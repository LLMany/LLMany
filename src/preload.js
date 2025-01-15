const { contextBridge, ipcRenderer } = require('electron');



const API = {
    sendToPython: (data) => ipcRenderer.invoke('to-python', data),

    onPythonMessage: (callback) => {
        ipcRenderer.on('from-python', (event, data) => callback(data));
        return () => {
            ipcRenderer.removeAllListeners('from-python');
        };
    }
}



contextBridge.exposeInMainWorld('electronAPI', API);