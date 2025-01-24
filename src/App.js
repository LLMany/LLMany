import './App.css';
import React, { useEffect, useState } from "react";
import Header from "./components/Header";
import MainContainer from "./components/MainContainer";
import { DEFAULT_MODEL, EMPTY_CHAT } from "./utils/constants";
import APIKeyModal from "./components/APIKeyModal";

export const Context = React.createContext();

function App() {
    const [currentModel, setCurrentModel] = useState(DEFAULT_MODEL);
    const [currentChatID, setCurrentChatID] = useState(EMPTY_CHAT);
    const [chatHistory, setChatHistory] = useState([])
    const [receivedData, setReceivedData] = useState([]); // State for received data
    const [messages, setMessages] = useState([]);

    useEffect(() => {
    }, []);

    return (
        <Context.Provider
            value={{
                model: [currentModel, setCurrentModel],
                chatID: [currentChatID, setCurrentChatID],
                allChats: [chatHistory, setChatHistory],
                messageList: [messages, setMessages],
                pythonData: [receivedData, setReceivedData] // Provide received data in context
            }}
            className="max-h text-text bg-primary"
        >
            <Header />
            <MainContainer />
        </Context.Provider>
    );
}

export default App;
