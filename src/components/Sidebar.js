import ModelList from "./ModelList";
import HistoryList from "./HistoryList";

function Sidebar() {
    return (
        <div
            style={{
                flex: 1,
                background: '#31363F',
                borderRadius: '8px',
                height: '100%',
                padding: '4px',
            }}
        >
            <ModelList/>
            <HistoryList/>
        </div>
    )
}

export default Sidebar;