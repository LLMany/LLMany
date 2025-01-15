export const handleSendData = async (request) => {
    try {
        console.log(request);
        await window.electronAPI.sendToPython(request);
    } catch (error) {
        console.error('Error sending data:', error);
    }
};

export function handlePythonMessage() {
    window.electronAPI.onPythonMessage((data) => {
        console.log(data);
    })
}