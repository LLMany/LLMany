const { contextBridge, ipcRenderer } = require('electron');
console.log("DUPA")
contextBridge.exposeInMainWorld('electronAPI', {
    sendToPython: (data) => ipcRenderer.send('to-python', data),
    onPythonMessage: (callback) => {
        const listener = (event, data) => {
            console.log("In preload")
            callback(data);
        };
        ipcRenderer.on('from-python', listener);
        console.log("In preload2")
        return () => {
            ipcRenderer.removeListener('from-python', listener);
        };
    },
    invoke: (channel, ...args) => ipcRenderer.invoke(channel, ...args), // Add invoke if you need it
    removeAllListeners: (channel) => ipcRenderer.removeAllListeners(channel),
});