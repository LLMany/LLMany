export const handleSendData = async (request) => {
    try {
        console.log(request);
        window.electron.ipcRenderer.send('to-python', request)
    } catch (error) {
        console.error('Error sending data:', error);
    }
};

export async function handlePythonMessage() {
    window.electron.ipcRenderer.on('from-python', passReceivedObject);
}

const handlePythonData = (event, data) => {
    console.log("Renderer received: " + data)
};


export const passReceivedObject = (data) => {
    console.log("Renderer received: " + data)
    return data;
}