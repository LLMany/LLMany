import './App.css';
import React, {useEffect, useState} from "react"
import Header from "./components/Header";
import MainContainer from "./components/MainContainer";
import {DEFAULT_MODEL, EMPTY_CHAT, EMPTY_INPUT} from "./utils/constants";
import {handleSendData} from "./communication/requestHandlers";
import {allChatsRequest, chatHistoryRequest} from "./communication/requestCreators";

export const Context = React.createContext();

function App() {

    const [currentModel, setCurrentModel] = useState(DEFAULT_MODEL);
    const [currentChatID, setCurrentChatID] = useState(EMPTY_CHAT);

    useEffect(() => {



        // return window.electronAPI.onPythonMessage((data) => {
        //     setMessages(prev => [...prev, data]);
        // });
    }, []);



    return (
        <Context.Provider
            value={{
                model: [currentModel, setCurrentModel],
                chatID: [currentChatID, setCurrentChatID],
            }}
            className="App"
        >
            <Header/>
            <MainContainer/>
        </Context.Provider>

    );
}

export default App;
