import Sidebar from "./Sidebar";
import ChatBox from "./ChatBox";


function MainContainer() {
    return (
        <div style={{
            display: 'flex',
            flexDirection: 'row',
            gap: '8px',
            height: '500px',
        }}>
            <Sidebar/>
            <ChatBox/>
        </div>
    )
}

export default MainContainer;