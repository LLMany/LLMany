import { useCallback, useContext, useEffect, useState } from "react";
import { Context } from "../App";
import HistoryElement from "./HistoryElement";
import { placeholderChats } from "../utils/placeholderData";
import { EMPTY_CHAT } from "../utils/constants";
import { handlePythonMessage } from "../communication/requestHandlers";
import { allChatsRequest } from "../communication/requestCreators";
import message from "./Message";

function HistoryList() {
  const [chatHistory, setChatHistory] = useState(placeholderChats);
  const { chatID } = useContext(Context);

  const handleReceivedData = useCallback((data) => {
    console.log("Received in React:", data);
    if (Array.isArray(data)) { // Check if data is an array
        setChatHistory(data);
        if (data.length > 0) {
          setCurrentChatID(data[0].chatID)
        }
    } else {
        console.error("Received data is not an array:", data);
        // Handle the error appropriately, e.g., set an error state
    }
}, [setCurrentChatID]); // Add setCurrentChatID as a dependency


  useEffect(() => {
        if (window.electronAPI) {
            window.electronAPI.sendToPython(allChatsRequest());
            const removeListener = window.electronAPI.onPythonMessage(handleReceivedData);

            return () => {
                removeListener();
            };
        }
    }, [handleReceivedData]);


    useEffect(() => {
    if (window.electronAPI) {
      const handleReceivedData = (data) => {
        console.log("Received in React:", data);
        // Update your state with received messages (e.g., setChatHistory)
        ; // Assuming data contains chat information
      };

      window.electronAPI.sendToPython(allChatsRequest()); // Send request
      const removeListener = window.electronAPI.onPythonMessage(handleReceivedData);

      return () => {
        removeListener();
      };
    }
  }, [chatID]);

  const chatsList = chatHistory.map((chat) => (
    <HistoryElement
      key={chat.chatID} // Add a key prop for better performance
      chatID={chat.chatID}
      selected={chatID === chat.chatID}
      onClick={() => setCurrentChatID(chat.chatID)}
    />
  ));

  return (
    <div style={{ display: "flex", flexDirection: "column", fontWeight: "bold", gap: "4px" }}>
      <br />
      History
      {chatsList}
    </div>
  );
}

export default HistoryList;
