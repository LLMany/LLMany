import {useState} from "react";
import {EMPTY_INPUT} from "../utils/constants";

function Input({onSubmit}) {

    const [input, setInput] = useState(EMPTY_INPUT);

    return (
        <div className="flex flex-row w-full space-x-2 p-2">
            <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                className="w-full bg-secondary rounded-full px-3 py-1"></input>
            <button
                className="bg-header hover:bg-button rounded-full px-3 font-semibold transition-colors duration-300"
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