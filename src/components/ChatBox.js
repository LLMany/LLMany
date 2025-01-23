import Chat from "./Chat";
import Input from "./Input";
import {useContext, useEffect, useState} from "react";
import {Context} from "../App";
import {EMPTY_CHAT, EMPTY_INPUT, MODEL_MESSAGE, USER_MESSAGE} from "../utils/constants";
import {placeholderMessages} from "../utils/placeholderData";
import EmptyChat from "./EmptyChat";
import {getAllChats, getNewChatID, sendMessageToChat} from "../communication/requestHandlers";
import {modelMap} from "../utils/values";


function ChatBox() {

    const {model, chatID, messageList, allChats} = useContext(Context);

    const [currentModel] = model;
    const [chatHistory, setChatHistory] = allChats;
    const [currentChatID, setCurrentChatID] = chatID;
    const [messages, setMessages] = messageList;

    useEffect(() => {
        console.log("---------------");
        console.log(messages)
        console.log("---------------");
    },[messages])

    const addMessageToChat = (responseMessage) => {
        console.log("DUPSKO" + JSON.stringify(responseMessage))
        setMessages((prevMessages) => [...prevMessages, responseMessage]);
    }

    const refreshMessages = (newMessages) => {
        setMessages(newMessages);
    }

    const addUserMessage = (message) => {
        return {
            role: USER_MESSAGE,
            content: message,
        }
    }


    const onSendMessage = async (message) => {
        if (message === EMPTY_INPUT) {
            return;
        }
        addMessageToChat(addUserMessage(message));
        if (currentChatID === EMPTY_CHAT) {
            let modelProvider = modelMap[currentModel].provider;
            await getNewChatID(modelProvider, currentModel, setCurrentChatID);
            getAllChats(setChatHistory)
            sendMessageToChat(currentChatID, message, addMessageToChat);
        } else {
            sendMessageToChat(currentChatID, message, addMessageToChat);
        }
    }

    return (
        <div style={{
            flex: 3,
            padding: '4px',
            background: '#31363F',
            borderRadius: '8px',
            height: '100%',
            display: 'flex',
            gap: '8px',
            flexDirection: 'column',
        }}>
            { currentChatID === EMPTY_CHAT ?
                <EmptyChat />  :
                <Chat messages={messages} />
            }
            <Input onSubmit={onSendMessage} />
        </div>
    )
}

export default ChatBox;
