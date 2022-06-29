import "./navbar.css";
import Notification from "../../img/notification-icon.svg";
import Message from "../../img/message.svg";
import chat from "../../img/chat2.svg";
import ChatModal from "../modal/chat-modal.js"
import { useEffect, useState } from "react";

const Navbar = ({ socket, user }) => {

  
    const [notifications, setNotifications] = useState([]);
    const [open, setOpen] = useState(false);
    const [chatModal, setChatModal] = useState(false)
    
  
    useEffect(() => {
      socket.on("getNotification", (data) => {
        console.log("getNoticaasdfas; ", data)
        setNotifications((prev) => [...prev, data]);
      });
    }, [socket]);
  
    const displayNotification = ({ senderName, type }) => {

      let action;
  
      if (type === 1) {
        action = "liked";
      } else if (type === 2) {
        action = "commented";
      } else {
        action = "shareded";
      }
      return (
        <span className="notification">{`${senderName} ${action} your post.`}</span>
      );
    };
  
    const handleRead = () => {
      setNotifications([]);
      setOpen(false);
    };
  
    return (
      <div className="navbar">
        
      {chatModal && <ChatModal setOpenModal={setChatModal} socket={socket} user={user}/>}

        <span className="logo">App</span>
        <div className="icons">
          <div className="icon" onClick={() => setOpen(!open)}>
            <img src={Notification} className="iconImg" alt="" />
            {
               notifications.length >0 &&
              <div className="counter">{notifications.length}</div>
            }
          </div>
          <div className="icon" onClick={() => setOpen(!open)}>
            <img src={Message} className="iconImg" alt="" />
          </div>
          <div className="icon" onClick={() => setChatModal(true)}>
            <img src={chat} className="iconImg" alt="" />
          </div>
        </div>
        {open && (
          <div className="notifications">
            {notifications.map((n) => displayNotification(n))}
            <button className="nButton" onClick={handleRead}>
              Mark as read
            </button>
          </div>
        )}
      </div>
    );
  };

export default Navbar