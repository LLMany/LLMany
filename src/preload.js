const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    // Send data to Python
    sendToPython: (data) => ipcRenderer.invoke('to-python', data),

    // Register handler for receiving data from Python
    onPythonMessage: (callback) => {
        ipcRenderer.on('from-python', (event, data) => callback(data));
        // Return cleanup function
        return () => {
            ipcRenderer.removeAllListeners('from-python');
        };
    }
});