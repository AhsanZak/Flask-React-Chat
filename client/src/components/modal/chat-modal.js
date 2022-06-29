import React, { useEffect, useState } from "react";
import "./chat-modal.css";
import $ from "jquery";

function ChatModal({setOpenModal, socket, user}){
    console.log("This is Adding post modal");

    socket.on("connect", (data) => {
        socket.send("User has Connected");
      });

    const [message, setMessage] = useState("");

    const SentMessage = () => {
        console.log("This is the new Chat : ", message);
        socket.send(message);
        $("#myMessage").val("")
    }

    useEffect(() => {
        socket.on("message", (data) => {
            console.log("this is messafe data ", data);
          setMessage(data);
            $("#messages").append('<p><span id="p-username">'+''+'</span>'+data+'</p>')
        });
      }, [socket]);

    return(

        <div id="myModal" className="modal">

        <div className="modal-content">
            <span className="close" onClick={ () => setOpenModal(false)}>&times;</span>
            <div className="modal-body">
                <ul id="messages"></ul>
            </div>
            <input id="myMessage" className="input-class" placeholder="Type here ... " onChange={(e) => setMessage(e.target.value)}></input>
            <button className="save-btn" onClick={SentMessage}>Sent</button>
        </div>

        </div>

    )

}

export default ChatModal;