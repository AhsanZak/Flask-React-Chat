from flask_socketio import SocketIO, emit, send, join_room, leave_room
from flask import Flask, render_template, url_for, copy_current_request_context, jsonify, request
from random import random
from time import sleep
from threading import Thread, Event
from flask_cors import CORS, cross_origin
import json
from dbconnect import insert

__author__ = 'slynn'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

online_user = {}

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True, cors_allowed_origins='*')



def remove_user(socketId):
    for i in online_user:
        print(" i ", i)

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')


@socketio.on('addPost')
def add_post(data):
    username = data["senderName"]
    postUrl = data["postUrl"]
    userImg = "https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500"
    # sql = f"INSERT INTO POSTS(username,fullname, userImg, postImg) VALUES({username},{username},{userImg},{postUrl})"
    # result = insert(sql)
    # Opening JSON file
    new_dict = {}
    new_dict["id"] = 1
    new_dict["username"] = username
    new_dict["fullname"] = "Test" + username
    new_dict["userImg"] = userImg
    new_dict["postImg"] = postUrl

    f_path = r'C:\Users\ahsan\OneDrive\Desktop\New folder\flask-react-chat\client\src\datas.json'
    
    with open(f_path, "r") as readfile:
        data = json.load(readfile)

    data.append(new_dict)

    json_object = json.dumps(data)

    with open(f_path, "w") as outfile:
        outfile.write(json_object)



@socketio.on('message')
def handleMessage(msg):
    currentSocketId = request.sid
    username = online_user[currentSocketId]
    send({"message":msg, "username":username}, broadcast=True)


@socketio.on('connect')
def test_connect(data):
    print("someone has connected ----------------------------- ", data)


@socketio.on('newUser')
def add_new_user(username):
    currentSocketId = request.sid
    if username not in online_user:
        online_user[currentSocketId] = username
    join_room("room"+username)
    print("THis is new user : ", username, online_user)


def get_reciever_id(reciever_name):
    
    # list out keys and values separately
    key_list = list(online_user.keys())
    val_list = list(online_user.values())
    
    position = val_list.index(reciever_name)
  
    
    # finding duplicate values
    # from dictionary using flip
    # flipped = {}
    
    # for key, value in online_user.items():
    #     if value not in flipped:
    #         flipped[value] = [key]
    #     else:
    #         flipped[value].append(key)
    
    # # printing result
    # print("final_dictionary", str(flipped))

    return key_list[position]


@socketio.on('sendNotification')
def test_connect(data):
    
    currentSocketId = request.sid
    print("-------------------Notification function current socket ID : ", currentSocketId)

    senderName = data["senderName"]
    receiverName = data["receiverName"]
    type_of_notification = data["type"]

    client_id = get_reciever_id(receiverName)
    
    print("These are the sende Notification details : =----------------------- ", online_user)

    result_dict = {"senderName": senderName, "type": type_of_notification}

    emit("getNotification", (result_dict), room="room"+receiverName)


@socketio.on('getNotification')
def handle_my_custom_event(data):
    print("This is handle custom event : ", data)
    emit('my response', data, broadcast=True)


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected ---------------------')


if __name__ == '__main__':
    CORS(app)
    socketio.run(app)
