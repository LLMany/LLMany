import Chat from "./Chat";
import Input from "./Input";
import {useContext, useState} from "react";
import {Context} from "../App";
import {EMPTY_CHAT, EMPTY_INPUT, MODEL_MESSAGE, USER_MESSAGE} from "../utils/constants";
import {placeholderMessages} from "../utils/placeholderData";
import EmptyChat from "./EmptyChat";
import {getNewChatID} from "../communication/requestHandlers";
import {modelMap} from "../utils/values";


function ChatBox() {

    const {model, chatID} = useContext(Context);

    const [currentModel, setCurrentModel] = model;
    const [currentChatID, setCurrentChatID] = chatID;
    const [messages, setMessages] = useState(placeholderMessages);

    // Send OnClick function to children for sending messages and fetching response
    const onSendMessage = (message) => {
        if (message === EMPTY_INPUT) {
            return;
        }
        if (currentChatID === EMPTY_CHAT) {
            let modelProvider = modelMap[currentModel].provider;
            setCurrentChatID(getNewChatID(modelProvider, currentModel));
            // Add chat to history
        }
        const newUserMessage = {owner: USER_MESSAGE, content: message};
        const modelResponse = {owner: MODEL_MESSAGE, content: "Response"};
        // handleSendData(messageRequest(currentChatID, inputData));
        setMessages(prevState =>
            [...prevState, newUserMessage, modelResponse] );

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