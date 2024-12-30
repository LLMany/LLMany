import ModelMessage from "./message/ModelMessage";
import UserMessage from "./message/UserMessage";

function Chat() {
    return (
        <div className="Chat">
            <ModelMessage message="No siema" />
            <UserMessage message="Hello World!" />
        </div>
    )
}

export default Chat;