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
            style={{
                overflowY: "scroll",
                padding: "4px",
                display: 'flex',
                flexDirection: 'column',
                height: '100%',
                width: '100%',
                gap: '4px',
            }}
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
