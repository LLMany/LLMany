import ModelElement from "./ModelElement";
import {useContext, useState} from "react";
import {Context} from "../App"
import {modelList} from "../utils/values";

function ModelList() {

    const {model} = useContext(Context);

    const [currentModel, setCurrentModel] = model;

    const listItems = modelList.map((model) => {
        return <ModelElement
            modelName={model}
            selected={currentModel === model}
            onClick={() => setCurrentModel(model)}
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