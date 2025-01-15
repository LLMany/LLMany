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
contextBridge.exposeInMainWorld('electron', { // Expose to window.electron
    ipcRenderer: {
      invoke: (channel, ...args) => ipcRenderer.invoke(channel, ...args),
      send: (channel, ...args) => ipcRenderer.send(channel, ...args), // If you need send
      on: (channel, func) => ipcRenderer.on(channel, func),
      removeAllListeners: (channel) => ipcRenderer.removeAllListeners(channel), // Important for cleanup
      // ... other methods you need
    },
  });