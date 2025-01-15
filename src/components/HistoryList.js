import {useCallback, useContext, useEffect, useState} from "react"
import {Context} from "../App"
import HistoryElement from "./HistoryElement"
import {placeholderChats} from "../utils/placeholderData"
import {EMPTY_CHAT} from "../utils/constants"
import {handlePythonMessage, handleResponse, handleSendData} from "../communication/requestHandlers";
import {allChatsRequest} from "../communication/requestCreators";

function HistoryList() {

    const [chatHistory, setChatHistory] = useState(placeholderChats)
    const {chatID} = useContext(Context)


    const [currentChatID, setCurrentChatID] = chatID

    useEffect(() => {
        console.log("Effect invoked.")
        handleSendData(allChatsRequest()).then()
        handlePythonMessage()
    }, [chatID])


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
            History
            {chatsList}
        </div>
    )
}

export default HistoryList;