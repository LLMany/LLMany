import {modelList, modelMap} from "../utils/values";
import KeyHandlingRow from "./KeyHandlingRow";
import {checkAPIKey} from "../communication/requestHandlers";
import {useState} from "react";

function APIKeyModal({open, onClose}) {

    const APIKeyRows = modelList.map((model) => {
        return <KeyHandlingRow
            key={model}
            model={model}
       />
    })

    return (
        <div
            className={
                `fixed inset-0 flex justify-center items-center transition-colors 
                ${open ? 'visible bg-black/40' : 'invisible'}`
            }
        >
            <div className={
                `bg-bgPrimary rounded-xl shadow transition-all 
                ${open ? 'scale-100 opacity-100' : 'scale-125 opacity-0'}`
            }>
                <div className="flex flex-col w-full space-y-1">
                    <div className={`flex flex-row justify-between font-bold bg-header p-4 rounded-t-xl`}>
                        Add/Edit/Delete existing API keys.
                        <button
                            onClick={onClose}
                        >
                            X
                        </button>
                    </div>
                    <div className={`p-4`}>
                        {APIKeyRows}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default APIKeyModal;