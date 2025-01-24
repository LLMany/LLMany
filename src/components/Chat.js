import ModelMessage from "./message/ModelMessage";
import UserMessage from "./message/UserMessage";
import {USER_MESSAGE} from "../utils/constants";

function Chat({messages}) {
    const messagesWithKeys = [];

    for (let i = 0; i < messages.length; i++) {
        messagesWithKeys.push({
            ...messages[i], // Spread the existing properties
            key: i.toString(), // Add the key property (important: must be a string)
        });
    }

    return (
        <div
            className="max-h text-text bg-primary h-full w-full bg-transparent p-3"
        >
            {
                messagesWithKeys.map(({role, content, key}) => (
                    <div key = {key}>
                    {role === USER_MESSAGE ? ( // Access message.role
                        <UserMessage message={content} /> // Access message.content
                        ) : (
                        <ModelMessage message={content} /> // Access message.content
                        )}
                    </div>
                ))
            }
        </div>
    )
}

export default Chat;
