import {addAPIKeyRequest, checkAPIKeyRequest} from "../communication/requestCreators";
import {modelMap} from "../utils/values";
import {GEMINI} from "../utils/constants";
import {useState} from "react";
import APIKeyModal from "./APIKeyModal";

function Header() {

    const [modalOpen, setModalOpen] = useState(false);

    const addKey = () => {
        setModalOpen(true);
    }

    const checkKey = () => {
        window.electronAPI.sendToPython(checkAPIKeyRequest(modelMap[GEMINI].provider))
    }
    return (
        <div className = "flex flex-row font-bold justify-between items-center p-4 bg-header shadow w-full">
            <div className="text-2xl">LLMany</div>
            <div className="space-x-4 p-2 cursor-pointer">
                <button onClick={addKey}>Add API key</button>
            </div>
            <APIKeyModal
                open={modalOpen}
                onClose={() => setModalOpen(false)}
            />
        </div>
    )
}

export default Header;