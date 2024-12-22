import './App.css';
import {useState} from "react"

function App() {

    const [currentModel, changeModel] = useState(null);
    const [loading, setLoading] = useState(false);
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState([]);



    return (
        <div className="App">
                <Header/>
                <MainBox/>
        </div>
    );
}

function Header() {
    return (
        <h3 className="Header">LLMany</h3>
    )
}

function Sidebar() {
    return (
        <div className="Sidebar">
            <ModelList/>
            <HistoryList/>
        </div>
    )
}

function ModelList() {
    return (
        <div className="ModelList"></div>
    )
}

function HistoryList() {
    return (
        <div className="HistoryList">
            <PlaceHolder/>
        </div>
    )
}

function Chat() {


    return (
        <div className="Chat">
        </div>
    )
}

function MainBox() {
    return (
        <div className="MainBox">
            <Sidebar/>
            <ChatBox/>
        </div>
    )
}


function PlaceHolder() {
    return (
        <h5>Empty container</h5>
    )
}

function ChatBox() {
    return (
        <div className="ChatBox">
            <Chat/>
            <Input/>
        </div>
    )
}


function Input() {
    return (
        <div className="Input">
            <textarea className="MessageInput"></textarea>
            <button className="SendButton">Send</button>
        </div>
    )
}

export default App;
