import Sidebar from "./Sidebar";
import ChatBox from "./ChatBox";


function MainContainer() {
    return (
        <div className={'flex flex-row max-h p-2 w-full bg-bgPrimary'}>
            <Sidebar/>
            <ChatBox/>
        </div>
    )
}

export default MainContainer;