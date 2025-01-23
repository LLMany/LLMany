import {placeholderChats} from "../utils/placeholderData";
import {EMPTY_CHAT, EMPTY_INPUT, USER_MESSAGE} from "../utils/constants";
import {chatHistoryRequest, messageRequest, newChatRequest} from "./requestCreators";
import message from "../components/Message";


export const getAllChats = (setChatHistory) => {
    let chats = [];
    window.electronAPI.sendToPython({"type": "all_chats"})
    window.electronAPI.onPythonMessage((data)=> {
        let receivedObject = JSON.parse(data);
        console.log(receivedObject + receivedObject.type + receivedObject.chats);
        if (receivedObject?.type === 'all_chats')
            chats = receivedObject?.chats ?? [];
        setChatHistory(chats);
    })
    console.log(chats);
    return chats;
}

export const getNewChatID = (modelProvider, model, setCurrentChatID) => {
    let newChatID = EMPTY_CHAT;
    window.electronAPI.sendToPython(newChatRequest(modelProvider, model));
    window.electronAPI.onPythonMessage((data)=> {
        let receivedObject = JSON.parse(data);
        if (receivedObject?.type === 'new_chat')
            newChatID = receivedObject?.chat_id ?? EMPTY_CHAT;
        setCurrentChatID(newChatID);
    })

    return newChatID
}


export const sendMessageToChat = (chatID, message, addResponse) => {
    let responseMessage = EMPTY_INPUT;
    console.log(" -> " + message);
    window.electronAPI.sendToPython(messageRequest(chatID, message));
    window.electronAPI.onPythonMessage((data)=> {
        console.log(" <- " + data);
        let receivedObject = JSON.parse(data);
        if (receivedObject?.type === 'message')
            responseMessage = receivedObject?.content ?? EMPTY_INPUT;
        addResponse(responseMessage);
    })
}

export const getChatContent = (chatID, setMessages) => {
    let chatContent = [];
    window.electronAPI.sendToPython(chatHistoryRequest(chatID));
    window.electronAPI.onPythonMessage((data)=> {
        let receivedObject = JSON.parse(data);
        if (receivedObject?.type === 'chat_history')
            chatContent = receivedObject?.messages ?? [];
        setMessages(chatContent);
    })
}
