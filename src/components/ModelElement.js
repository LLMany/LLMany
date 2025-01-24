import {modelMap} from "../utils/values";
import {useEffect, useState} from "react";

function ModelElement({modelName, selected, onClick}) {

    const [mouseOver, setMouseOver] = useState(false);
    const displayName = modelMap[modelName].displayName;
    const highlightColor = modelMap[modelName].color
    const borderColorClass = selected ? `border-[${highlightColor}]` : "border-secondary";
    const bgColorClass = selected ? `bg-bgSecondary` : "bg-secondary";

    useEffect(() => {
        console.log("----->" + highlightColor);
    })
    return (
        <div
            className={`${borderColorClass} ${bgColorClass} hover:border-primary font-semibold px-3 py-1 rounded-md cursor-pointer border-2 border-secondary`}
            onClick={onClick}
        >
            {displayName}
        </div>
    )
}

export default ModelElement;