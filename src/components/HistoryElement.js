import {useState} from "react";

function HistoryElement({chatID, selected, onClick}) {

    const [mouseOver, setMouseOver] = useState(false);
    const bgColorClass = selected ? `bg-bgSecondary` : "bg-secondary";

    return (
        <div
            className={`border-secondary ${bgColorClass} hover:border-primary font-semibold px-3 py-1 rounded-md cursor-pointer border-2 border-secondary`}
            onClick={onClick}
            onMouseOver={() => setMouseOver(true)}
            onMouseLeave={() => setMouseOver(false)}
        >
            {chatID}
        </div>
    )
}

export default HistoryElement;