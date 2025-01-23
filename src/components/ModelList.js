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
        <>
            <div style={{
                display: 'flex',
                flexDirection: 'column',
                fontWeight: 'bold',
                gap: '4px',
            }}>
                Models
                {listItems}
            </div>
        </>
    )
}


    export default ModelList;
