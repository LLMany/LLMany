import {useState} from "react";
import {EMPTY_INPUT} from "../utils/constants";

function Input({onSubmit}) {

    const [input, setInput] = useState(EMPTY_INPUT);

    return (
        <div className="Input">
            <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                className="MessageInput"></input>
            <button
                className="SendButton"
                onClick={() => {
                    onSubmit(input);
                    setInput(EMPTY_INPUT);
                }
            }
            >Send
            </button>
        </div>
    )
}

export default Input;