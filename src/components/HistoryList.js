import {useCallback, useContext, useEffect, useState} from "react"
import {Context} from "../App"
import HistoryElement from "./HistoryElement"
import {placeholderChats} from "../utils/placeholderData"
import {EMPTY_CHAT} from "../utils/constants"
import {allChatsRequest} from "../communication/requestCreators";
import message from "./Message";
import {getAllChats} from "../communication/requestHandlers";

function HistoryList() {

    const [chatHistory, setChatHistory] = useState(placeholderChats)
    const {chatID} = useContext(Context)

    const [tempData, setTempData] = useState("DUPSKO")
    const [currentChatID, setCurrentChatID] = chatID

    useEffect(() => {
        getAllChats(setChatHistory)
        console.log(chatHistory)
    }, [chatID]); //


    const chatsList = chatHistory.map((chat) => {
        return <HistoryElement
            chatID={chat.chat_id}
            selected={currentChatID === chat.chat_id}
            onClick={() => setCurrentChatID(chat.chat_id)}
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
