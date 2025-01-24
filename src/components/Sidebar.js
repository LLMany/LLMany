import ModelList from "./ModelList";
import HistoryList from "./HistoryList";

function Sidebar() {
    return (
        <div
            className={'flex flex-col w-64 space-y-4'}
        >
            <ModelList/>
            <HistoryList/>
        </div>
    )
}

export default Sidebar;