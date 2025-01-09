import {useContext} from "react";
import {Context} from "../App";
import {modelMap} from "../utils/values";

function EmptyChat() {
    const {model} = useContext(Context);
    const [currentModel] = model;
    const displayName = modelMap[currentModel].displayName;

    return (
        <div style={{
            padding: '8px',
            width: '100%',
            height: '100%'
        }}
        >
            Send a message to the chat with {displayName}.
        </div>
    )
}

export default EmptyChat;