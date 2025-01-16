export const handleSendData = async (request) => {
    try {
        console.log(request);
        window.electron.ipcRenderer.send('to-python', request)
    } catch (error) {
        console.error('Error sending data:', error);
    }
};

export async function handlePythonMessage(data) {
    //window.electron.ipcRenderer.on('from-python', passReceivedObject);
    console.log("Renderer received: " + data)
}

const handlePythonData = (event, data) => {

};


export const passReceivedObject = (data) => {
    console.log("Renderer received: " + data)
    return data;
}