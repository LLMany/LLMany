import {useState} from "react";

function HistoryElement({chatID, selected, onClick}) {

    const [mouseOver, setMouseOver] = useState(false);

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
            {chatID}
        </div>
    )
}

export default HistoryElement;