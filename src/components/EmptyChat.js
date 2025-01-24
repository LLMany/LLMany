import {useContext} from "react";
import {Context} from "../App";
import {modelMap} from "../utils/values";

function EmptyChat() {
    const {model} = useContext(Context);
    const [currentModel] = model;
    const displayName = modelMap[currentModel].displayName;

    return (
        <div className={'content-center text-center w-full h-full text-primary font-semibold text-lg'}>
            Send a message to the chat with {displayName}.
        </div>
    )
}

export default EmptyChat;