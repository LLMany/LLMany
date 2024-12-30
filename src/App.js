import './App.css';
import {useEffect, useState} from "react"
import Header from "./components/Header";
import MainContainer from "./components/MainContainer";

function App() {

    const [currentModel, setCurrentModel] = useState(null);
    const [loading, setLoading] = useState(false);
    const [inputData, setInputData] = useState("");
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        // Subscribe to Python messages
        const cleanup = window.electronAPI.onPythonMessage((data) => {
            setMessages(prev => [...prev, data]);
        });

        // Cleanup subscription on unmount
        return cleanup;
    }, []);

    const handleSendData = async () => {
        try {
            const data = { message: inputData };
            await window.electronAPI.sendToPython(data);
            setInputData('');
        } catch (error) {
            console.error('Error sending data:', error);
        }
    };

    return (
        <div className="App">
                <Header/>
                <MainContainer/>
        </div>
    );
}

export default App;
