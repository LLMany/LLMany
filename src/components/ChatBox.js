import Chat from "./Chat";
import Input from "./Input";

function ChatBox() {
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
            <Chat/>
            <Input/>
        </div>
    )
}

export default ChatBox;