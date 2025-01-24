import {useCallback, useContext, useEffect, useState} from "react"
import {Context} from "../App"
import HistoryElement from "./HistoryElement"
import {placeholderChats} from "../utils/placeholderData"
import {EMPTY_CHAT} from "../utils/constants"
import {allChatsRequest} from "../communication/requestCreators";
import message from "./Message";
import {getAllChats, getChatContent, getNewChatID} from "../communication/requestHandlers";
import {modelMap} from "../utils/values";

function HistoryList() {

    const [chatHistory, setChatHistory] = useState(placeholderChats)
    const {chatID, model, messageList} = useContext(Context)

    const [currentChatID, setCurrentChatID] = chatID
    const [currentModel, setCurrentModel] = model
    const [messages, setMessages] = messageList


    useEffect(() => {
        getAllChats(setChatHistory)
        getChatContent(currentChatID, setMessages)
    }, [currentChatID]); //

    const addNewChat = () => {
        setCurrentChatID(EMPTY_CHAT)
    }

    const chatsList = chatHistory.map((chat) => {
        return <HistoryElement
            key={chat.chat_id}
            chatID={chat.chat_id}
            selected={currentChatID === chat.chat_id}
            onClick={() => {
                setCurrentChatID(chat.chat_id)
                setCurrentModel(chat.model)
            }}
        />
    })

    return (
        <div className={'flex flex-col max-h p-1 pb-3 rounded-md bg-bgSecondary'}>
            <div className={'flex flex-row max-h justify-between px-1 pb-2 pt-1 font-bold  text-white'}>
                History
                <button onClick={addNewChat}>+</button>
            </div>
            <div className={'flex flex-col h-72 overflow-y-scroll space-y-1 justify-start'}>
                {chatsList}
            </div>
        </div>

    )
}

export default HistoryList;
