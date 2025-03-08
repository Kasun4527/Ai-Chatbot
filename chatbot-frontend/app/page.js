"use client";

import { useState } from "react";
import axios from "axios";

export default function Chatbot() {
  const [message, setMessage] = useState("");  // Stores user input
  const [response, setResponse] = useState("");  // Stores chatbot's response

  const sendMessage = async () => {
    if (!message) {
      console.log("No message entered!");
      return;
    }

    console.log("Sending message:", message);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", { message });
      console.log("Response received:", res.data);  // Debugging response
      setResponse(res.data.response);
    } catch (error) {
      console.error("Error:", error);
      setResponse("Failed to get response. Please try again.");
    }
  };

  return (
    <div>
      <h1>Chatbot</h1>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type a message..."
      />
      <button onClick={sendMessage}>Send</button> {/* ✅ Send button */}
      <p><strong>Chatbot:</strong> {response}</p> {/* ✅ Displays chatbot's actual response */}
    </div>
  );
}
