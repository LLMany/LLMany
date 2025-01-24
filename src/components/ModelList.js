import ModelElement from "./ModelElement";
import {useContext, useState} from "react";
import {Context} from "../App"
import {modelList} from "../utils/values";
import {EMPTY_CHAT} from "../utils/constants";

function ModelList() {

    const {model, chatID} = useContext(Context);

    const [currentModel, setCurrentModel] = model;
    const [currentChatID, setCurrentChatID] = chatID

    const listItems = modelList.map((model) => {
        return <ModelElement
            key={model}
            modelName={model}
            selected={currentModel === model}
            onClick={() => {
                setCurrentModel(model)
                setCurrentChatID(EMPTY_CHAT)
            }
            }
        />;
    });

    return (
        <div className={'flex flex-col max-h p-1 rounded-md bg-bgSecondary'}>
            <div className={'flex flex-row max-h justify-between px-1 pb-2 pt-1 font-bold  text-white'}>
                Models
            </div>
            <div className={'flex flex-col overflow-y-scroll space-y-1'}>
                {listItems}
            </div>
        </div>
    )
}


export default ModelList;
