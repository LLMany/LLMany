import {modelMap} from "../utils/values";
import {useState} from "react";

function ModelElement({modelName, selected, onClick}) {

    const [mouseOver, setMouseOver] = useState(false);
    const displayName = modelMap[modelName].displayName;


    return (
        <div
            style={{
                flex: 1,
                borderRadius: '8px',
                padding: '4px',
                background: selected ? '#666666' : '#444444',
                color: 'white',
                cursor: 'pointer',
                border: mouseOver ? '2px solid white' : '2px solid #666666',
            }}
            onClick={onClick}
            onMouseOver={() => setMouseOver(true)}
            onMouseLeave={() => setMouseOver(false)}
        >
            {displayName}
            <br/>
            {selected ? <> chat key... </> : <> </>}
        </div>
    )
}

export default ModelElement;