import {addAPIKeyRequest, checkAPIKeyRequest} from "../communication/requestCreators";
import {modelMap} from "../utils/values";
import {GEMINI} from "../utils/constants";

function Header() {

    const addKey = () => {
        const key = "AIzaSyBUlxJNVT5DsxOf4EkujnNBHcW6nwWdXno"
        window.electronAPI.sendToPython(addAPIKeyRequest(modelMap[GEMINI].provider), key)
    }

    const checkKey = () => {
        window.electronAPI.sendToPython(checkAPIKeyRequest(modelMap[GEMINI].provider))
    }
    return (
        <h3
            style={{
                paddingLeft: '8px',
                display: 'flex',
                flexDirection: 'row',
            }}
        >
            LLMany
            <button onClick={addKey}>Add API key</button>
            <button onClick={checkKey}>Check API key</button>
        </h3>
    )
}

export default Header;