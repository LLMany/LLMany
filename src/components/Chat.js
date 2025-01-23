import ModelMessage from "./message/ModelMessage";
import UserMessage from "./message/UserMessage";
import {USER_MESSAGE} from "../utils/constants";

function Chat({messages}) {


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
                messages.map(({owner, content}) => (
                    <div key = {content}>
                    {owner === USER_MESSAGE ? ( // Access message.role
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
