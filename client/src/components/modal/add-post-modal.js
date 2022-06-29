import React, { useState } from "react";
import "./add-post-modal.css";

function PostModal({setOpenModal, socket, user}){
    console.log("This is Adding post modal");

    const [postUrl, setPostUrl] = useState("");
    const save_post = () => {
        console.log("This is the new POST URL : ", postUrl);

        socket.emit("addPost", {
            senderName: user,
            postUrl: postUrl
          });

          setOpenModal(false);
    }

    return(

        <div id="myModal" className="modal">

        <div className="modal-content">
            <span className="close" onClick={ () => setOpenModal(false)}>&times;</span>
            <p>Provide the URL for the post</p>
            <input className="input-class" placeholder="Paste the url here : " onChange={(e) => setPostUrl(e.target.value)}></input>
            <button className="save-btn" onClick={save_post}>Save</button>
        </div>

        </div>

    )

}

export default PostModal