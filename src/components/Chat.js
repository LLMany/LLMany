import ModelMessage from "./message/ModelMessage";
import UserMessage from "./message/UserMessage";
import {USER_MESSAGE} from "../utils/constants";

function Chat({messages}) {


    return (
        <div
            className="max-h text-text bg-primary h-full w-full bg-transparent p-3"
        >
            {
                messages.map(({role, content}) => (
                    <div key = {content}>
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
