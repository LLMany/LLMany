import {useCallback, useContext, useEffect, useState} from "react"
import {Context} from "../App"
import HistoryElement from "./HistoryElement"
import {placeholderChats} from "../utils/placeholderData"
import {EMPTY_CHAT} from "../utils/constants"
import {
    handlePythonMessage,
    handleResponse,
    handleSendData,
    passReceivedObject
} from "../communication/requestHandlers";
import {allChatsRequest} from "../communication/requestCreators";
import message from "./Message";

function HistoryList() {

    const [chatHistory, setChatHistory] = useState(placeholderChats)
    const {chatID} = useContext(Context)

    const [tempData, setTempData] = useState(0)
    const [currentChatID, setCurrentChatID] = chatID

    const tempFunc = async () => {
        // let temp = window.electronAPI.fetchData().then(function(result) {
        //     console.log(result)
        //     setTempData(result)
        // })
        let temp = await window.electronAPI.sendToPython(allChatsRequest())

        console.log("sendToPython", temp)
    }

    useEffect(() => {

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
            <button onClick={tempFunc}>{tempData}</button>
            History
            {chatsList}
        </div>
    )
}

export default HistoryList;