import Chat from "./Chat";
import Input from "./Input";
import { useContext, useState } from "react";
import { Context } from "../App";
import { EMPTY_CHAT, EMPTY_INPUT, MODEL_MESSAGE, USER_MESSAGE } from "../utils/constants";
import { placeholderMessages } from "../utils/placeholderData";
import EmptyChat from "./EmptyChat";
import { getNewChatID, sendMessageToChat } from "../communication/requestHandlers";
import { modelMap } from "../utils/values";


function ChatBox() {

    const { model, chatID } = useContext(Context);

    const [currentModel] = model;
    const [currentChatID, setCurrentChatID] = chatID;
    const [messages, setMessages] = useState(placeholderMessages);

    const addResponse = (responseMessage) => {
        console.log("DUPA")
        console.log("CZY DUPA " + JSON.stringify(responseMessage))
        setMessages((prevMessages) => [...prevMessages, responseMessage]);
    }

    // Send OnClick function to children for sending messages and fetching response
    const onSendMessage = (message) => {
        if (message === EMPTY_INPUT) {
            return;
        }
        if (currentChatID === EMPTY_CHAT) {
            let modelProvider = modelMap[currentModel].provider;
            getNewChatID(modelProvider, currentModel, setCurrentChatID);
            // Add chat to history
        }
        sendMessageToChat(currentChatID, message, addResponse);
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
            {currentChatID === EMPTY_CHAT ?
                <EmptyChat /> :
                <Chat messages={messages} />
            }
            <Input onSubmit={onSendMessage} />
        </div>
    )
}

export default ChatBox;
