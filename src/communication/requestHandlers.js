

export const handleSendData = async (request) => {
    try {
        // await window.electronAPI.sendToPython(request);
        console.log(request);
    } catch (error) {
        console.error('Error sending data:', error);
    }
};