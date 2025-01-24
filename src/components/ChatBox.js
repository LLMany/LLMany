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


    const handleMessages = (userMessageContent, modelResponse) => {
        setMessages(prevMessages => {
            const newMessages = [
                ...prevMessages,
                { role: USER_MESSAGE, content: userMessageContent },
                ...(modelResponse ? [{ role: MODEL_MESSAGE, ...modelResponse }] : []), // Add model response if available
            ];
            return newMessages;
        });
    };
    
    const addMessageToChat = (responseMessage) => {
        setMessages((prevMessages) => {
            const newMessages = [...prevMessages, responseMessage];
            return newMessages;
        });
    };

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
            const newChatID = await getNewChatID(modelProvider, currentModel, setCurrentChatID);
            console.log("NEW CHAT ID" + newChatID);
            getAllChats(setChatHistory)
            sendMessageToChat(newChatID, message, addMessageToChat);
        } else {
            sendMessageToChat(currentChatID, message, addMessageToChat);
        }
    }

    return (
        <div className={'flex flex-col max-h w-full ml-2 bg-bgSecondary rounded-md'}>
            { currentChatID === EMPTY_CHAT ?
                <EmptyChat />  :
                <Chat messages={messages} />
            }
            <Input onSubmit={onSendMessage} />
        </div>
    )
}

export default ChatBox;
