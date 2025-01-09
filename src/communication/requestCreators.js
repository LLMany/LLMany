export function messageRequest(chatID, message) {
    return JSON.stringify(
        {
            type: "messageRequest",
            chat_id: chatID,
            contents: message
        });
}

export function newChatRequest(modelType, model) {
    return JSON.stringify(
        {
            type: "new_chat",
            model_type: modelType,
            model: model
        }
    )
}

export function deleteChatRequest(chatID) {
    return JSON.stringify(
        {
            type: "delete_chat",
            chat_id: chatID,
        }
    )
}

export function allChatsRequest() {
    return JSON.stringify(
        {
            type: "all_chats",
        }
    )
}

export function chatHistoryRequest(chatID) {
    return JSON.stringify(
        {
            type: "chat_history",
            chat_id: chatID,
        }
    )
}

export function addAPIKeyRequest(modelType, apiKey) {
    return JSON.stringify(
        {
            type: "add_api_key",
            model_type: modelType,
            api_key: apiKey,
        }
    )
}

export function removeAPIKeyRequest(modelType) {
    return JSON.stringify(
        {
            type: "remove_api_key",
            model_type: modelType,
        }
    )
}

export function checkAPIKeyRequest(modelType) {
    return JSON.stringify(
        {
            type: "check_api_key",
            model_type: modelType,
        }
    )
}