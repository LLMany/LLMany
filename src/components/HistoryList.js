import {useCallback, useContext, useEffect, useState} from "react"
import {Context} from "../App"
import HistoryElement from "./HistoryElement"
import {placeholderChats} from "../utils/placeholderData"
import {EMPTY_CHAT} from "../utils/constants"
import {allChatsRequest} from "../communication/requestCreators";
import message from "./Message";
import {getAllChats, getNewChatID} from "../communication/requestHandlers";
import {modelMap} from "../utils/values";

function HistoryList() {

    const [chatHistory, setChatHistory] = useState(placeholderChats)
    const {chatID, model} = useContext(Context)

    const [currentChatID, setCurrentChatID] = chatID
    const [currentModel, setCurrentModel] = model



    useEffect(() => {
        getAllChats(setChatHistory)
    }, [chatID]); //

    const addNewChat = () => {
        setCurrentChatID(EMPTY_CHAT)
    }

    const chatsList = chatHistory.map((chat) => {
        return <HistoryElement
            chatID={chat.chat_id}
            selected={currentChatID === chat.chat_id}
            onClick={() => {
                setCurrentChatID(chat.chat_id)
                setCurrentModel(chat.model)
            }}
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
            <button onClick={addNewChat}>New chat</button>
            {chatsList}
        </div>
    )
}

export default HistoryList;
