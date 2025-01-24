import {modelList, modelMap} from "../utils/values";
import {EMPTY_INPUT} from "../utils/constants";
import {useEffect, useState} from "react";
import {addAPIKey, checkAPIKey, removeAPIKey} from "../communication/requestHandlers";

function KeyHandlingRow({ model }) {

    const [keyExists, setKeyExists] = useState(false);
    const modelName = modelMap[model].displayName;
    const modelProvider = modelMap[model].provider;
    const [APIKey, setAPIKey] = useState(EMPTY_INPUT);

    useEffect(() => {
        checkAPIKey(modelMap[model].provider, setKeyExists);
        console.log(" KEY: " + keyExists + " " + model);
    })

    const removeAPIKeyLauncher = () => {
        removeAPIKey(modelProvider)
        setKeyExists(false);
    }

    const addAPIKeyLauncher = () => {
        addAPIKey(modelProvider, APIKey)
        setKeyExists(true);
    }


    return (
        <div
            className={'flex flex-row justify-between  space-x-4 py-2 content-center'}
        >
            <div className={ ` ${keyExists === true ? 'text-green-700' : 'text-red-700'} ` }>
                {keyExists ? "✔" : "X"}
            </div>
            <div>
                {modelName}
            </div>
            <div className = "space-x-4">
                <input
                    value={APIKey}
                    placeholder="Enter API key..."
                    className={"bg-secondary rounded-full px-3 py-1 text-white"}
                    onChange={(e) => {
                        setAPIKey(e.target.value)
                    }}
                />
                <button
                    onClick={() => {
                        addAPIKeyLauncher()
                        setAPIKey(EMPTY_INPUT)
                    }}
                >
                    Add
                </button>
                <button
                    className={'hover:text-failure'}
                    onClick={() => {
                        removeAPIKeyLauncher()
                    }}
                >
                    Delete
                </button>
            </div>
        </div>
    )
}

export default KeyHandlingRow;