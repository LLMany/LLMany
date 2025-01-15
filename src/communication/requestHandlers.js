export const handleSendData = async (request) => {
    try {
        console.log(request);
        window.electron.ipcRenderer.send('to-python', request)
    } catch (error) {
        console.error('Error sending data:', error);
    }
};

export function handlePythonMessage() {
    window.electron.ipcRenderer.on('from-python', handlePythonData);
}

const handlePythonData = (event, data) => {
    console.log(data)
};


