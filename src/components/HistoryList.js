import {useCallback, useContext, useEffect, useState} from "react"
import {Context} from "../App"
import HistoryElement from "./HistoryElement"
import {placeholderChats} from "../utils/placeholderData"
import {EMPTY_CHAT} from "../utils/constants"
import {allChatsRequest} from "../communication/requestCreators";
import message from "./Message";

function HistoryList() {

    const [chatHistory, setChatHistory] = useState(placeholderChats)
    const {chatID} = useContext(Context)

    const [tempData, setTempData] = useState("DUPSKO")
    const [currentChatID, setCurrentChatID] = chatID

    useEffect(() => {

        const handleFromPython = (event, message) => {
            // Update component state or perform actions with the received message
            console.log('Received from Python:', message);
            // For example, if you have a state variable 'messages':
            // setMessages(prevMessages => [...prevMessages, message]);
        };
        window.electronAPI.sendToPython({"type": "all_chats"})
        window.electronAPI.onPythonMessage((data)=> {setTempData(JSON.stringify(data))})
        // ipcRenderer.on('from-python', handleFromPython);

        // Important: Remove the listener when the component unmounts
        return () => {
            // ipcRenderer.removeListener('from-python', handleFromPython);
        };
    }, [chatID]); //


    const chatsList = chatHistory.map((chat) => {
        return <HistoryElement
            chatID={chat.chatID}
            selected={currentChatID === chat.chatID}
            onClick={() => setCurrentChatID(chat.chatID)}
        />
    })

    return (
        <div style={{
            display: "flex",
            flexDirection: "column",
            fontWeight: "bold",
            gap: "4px"
        }}>
            <br/>
            {tempData}
            History
            {chatsList}
        </div>
    )
}

export default HistoryList;
