import {EMPTY_CHAT, EMPTY_INPUT, GEMINI} from "../utils/constants";
import {
    addAPIKeyRequest,
    chatHistoryRequest,
    checkAPIKeyRequest,
    messageRequest,
    newChatRequest,
    removeAPIKeyRequest
} from "./requestCreators";
import {modelMap} from "../utils/values";


export const getAllChats = (setChatHistory) => {
    let chats = [];
    window.electronAPI.sendToPython({"type": "all_chats"})
    window.electronAPI.onPythonMessage((data) => {
        const receivedObject = JSON.parse(data);
        if (receivedObject?.type === 'all_chats') {
            chats = receivedObject?.chats ?? [];
            setChatHistory(chats);
        }
    })
}

export const getNewChatID = (modelProvider, model) => {
    return new Promise((resolve, reject) => {
        let newChatID = EMPTY_CHAT;

        // Send a request to Python
        window.electronAPI.sendToPython(newChatRequest(modelProvider, model));

        // Listen for the response from Python
        window.electronAPI.onPythonMessage((data) => {
            try {
                const receivedObject = JSON.parse(data);
                if (receivedObject?.type === 'new_chat') {
                    newChatID = receivedObject?.chat_id ?? EMPTY_CHAT;
                    resolve(newChatID); // Resolve the promise with the chat ID
                }
            } catch (error) {
                reject(error); // Reject the promise if JSON parsing fails
            }
        });
    });
};


export const sendMessageToChat = (chatID, message, addResponse) => {
    let responseMessage = EMPTY_INPUT;
    window.electronAPI.sendToPython(messageRequest(chatID, message));
    window.electronAPI.onPythonMessage((data) => {
        const receivedObject = JSON.parse(data);
        if (receivedObject?.type === 'message') {
            responseMessage = receivedObject?.content ?? EMPTY_INPUT;
            addResponse(responseMessage);
        }
    })
}

export const getChatContent = (chatID, setMessages) => {
    let chatContent = [];
    window.electronAPI.sendToPython(chatHistoryRequest(chatID));
    window.electronAPI.onPythonMessage((data) => {
        const receivedObject = JSON.parse(data);
        if (receivedObject?.type === 'chat_history') {
            chatContent = receivedObject?.messages ?? [];
            setMessages(chatContent);
        }
    })
}

export const checkAPIKey =  (provider, setKeyExists) => {
    console.log(" SENT KEY QUERY -> " + provider);
    window.electronAPI.sendToPython(checkAPIKeyRequest(provider))
    window.electronAPI.onPythonMessage((data) => {
        const receivedObject = JSON.parse(data);
        if (receivedObject?.type === 'check_api_key' && receivedObject?.model_type === provider) {
             const keyExists = receivedObject?.["exists"];
             setKeyExists(keyExists);
        }
    });
}

export const addAPIKey = (modelType, key) => {
    window.electronAPI.sendToPython(addAPIKeyRequest(modelType, key))
}

export const removeAPIKey = (modelType) => {
    window.electronAPI.sendToPython(removeAPIKeyRequest(modelType))
}