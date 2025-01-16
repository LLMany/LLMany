export function messageRequest(chatID, message) {
    return {
        type: "message",
        chat_id: chatID,
        contents: message
    }
}

export function newChatRequest(modelType, model) {
    return {
        type: "new_chat",
        model_type: modelType,
        model: model
    }
}

export function deleteChatRequest(chatID) {
    return {
        type: "delete_chat",
        chat_id: chatID,
    }
}

export function allChatsRequest() {
    return {
        type: "all_chats",
    }
}

export function chatHistoryRequest(chatID) {
    return {
        type: "chat_history",
        chat_id: chatID,
    }
}

export function addAPIKeyRequest(modelType, apiKey) {
    return {
        type: "add_api_key",
        model_type: modelType,
        api_key: apiKey,
    }
}

export function removeAPIKeyRequest(modelType) {
    return {
        type: "remove_api_key",
        model_type: modelType,
    }
}

export function checkAPIKeyRequest(modelType) {
    return {
        type: "check_api_key",
        model_type: modelType,
    }
}