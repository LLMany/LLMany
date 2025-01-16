import {placeholderChats} from "../utils/placeholderData";
import {EMPTY_CHAT} from "../utils/constants";
import {newChatRequest} from "./requestCreators";


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

export const getNewChatID = (modelProvider, model) => {
    let newChatID = EMPTY_CHAT;
    window.electronAPI.sendToPython(newChatRequest(modelProvider, model));
    window.electronAPI.onPythonMessage((data)=> {
        let receivedObject = JSON.parse(data);
        if (receivedObject?.type === 'new_chat')
            newChatID = receivedObject?.chat_id ?? EMPTY_CHAT;
    })

    return newChatID
}