import './App.css';
import React, { useEffect, useState } from "react";
import Header from "./components/Header";
import MainContainer from "./components/MainContainer";
import { DEFAULT_MODEL, EMPTY_CHAT } from "./utils/constants";

export const Context = React.createContext();

function App() {
    const [currentModel, setCurrentModel] = useState(DEFAULT_MODEL);
    const [currentChatID, setCurrentChatID] = useState(EMPTY_CHAT);
    const [receivedData, setReceivedData] = useState([]); // State for received data

    useEffect(() => {
        if (window.electronAPI) { // Check if electronAPI exists

            const handlePythonData = (data) => {
                console.log("Data from Python:", data);
                setReceivedData((prevData) => [...prevData, data]);
            };

            const removeListener = window.electronAPI.onPythonMessage(handlePythonData);

            return () => {
                removeListener(); // Correct cleanup using the removeListener function
            };
        }
    }, []);

    return (
        <Context.Provider
            value={{
                model: [currentModel, setCurrentModel],
                chatID: [currentChatID, setCurrentChatID],
                pythonData: [receivedData, setReceivedData] // Provide received data in context
            }}
            className="App"
        >
            <Header />
            <MainContainer />
        </Context.Provider>
    );
}

export default App;
