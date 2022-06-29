import { useEffect, useState } from "react";
import "./App.css";
// import Card from "./components/card/Card.js";
import Navbar from "./components/Navbar/navbar.js";
import Cards from "./components/Cards/card.js"
import post from "./datas.json";
import { io } from "socket.io-client";
import Add from "./img/add_icon.svg";
import Modal from "./components/modal/add-post-modal.js"
import { Container, Row, Col } from 'react-bootstrap';

const App = () => {
  const [username, setUsername] = useState("");
  const [user, setUser] = useState("");
  const [socket, setSocket] = useState(null);
  const [addModal, setAddModal] = useState(false);

  console.log("These are the posts : ", post);

  useEffect(() => {
    setSocket(io("http://localhost:5000"));
  }, []);

  useEffect(() => {
    socket?.emit("newUser", user);
  }, [socket, user]);
  
  return (
    <Container>
      <Row>
        <Col>
      {addModal && <Modal setOpenModal={setAddModal} socket={socket} user={user}/>}
      {user ? (
        <>
          <Navbar socket={socket} user={user}/>
          <div className="cards-container">
            {post.map((post) => (
              <Cards key={post.id} post={post} socket={socket} user={user}/>
            ))}
          </div>
          <span className="username">{user}</span>
          
          <div className="add-container">
            <img src={Add} className="addImg" alt="" onClick={ () => setAddModal(true)}/>
          </div>

        </>
      ) : (
        <div className="login">
          <h2>Mini App</h2>
          <input
            type="text"
            placeholder="username"
            onChange={(e) => setUsername(e.target.value)}
          />
          <button onClick={() => setUser(username)}>Login</button>
        </div>
      )}
      </Col>
      </Row>
      </Container>
    

  );
}
export default App;
