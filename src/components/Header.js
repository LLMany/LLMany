import {addAPIKeyRequest, checkAPIKeyRequest} from "../communication/requestCreators";
import {modelMap} from "../utils/values";
import {GEMINI} from "../utils/constants";

function Header() {

    const addKey = () => {
        const key = ""
        const request = addAPIKeyRequest(modelMap[GEMINI].provider, key)
        console.log(request)
        window.electronAPI.sendToPython(request)
    }

    const checkKey = () => {
        window.electronAPI.sendToPython(checkAPIKeyRequest(modelMap[GEMINI].provider))
    }
    return (
        <div className = "flex flex-row justify-between items-center m-2">
            <div className="font-bold ">LLMany</div>
            <div className="space-x-4">
                <button onClick={addKey}>Add API key</button>
                <button onClick={checkKey}>Check API key</button>
            </div>
        </div>
    )
}

export default Header;