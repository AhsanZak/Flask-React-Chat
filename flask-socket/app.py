from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context, jsonify, request
from random import random
from time import sleep
from threading import Thread, Event
from flask_cors import CORS, cross_origin
import json

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




@socketio.on('connect')
def test_connect(data):
    print("someone has connected ----------------------------- ")


@socketio.on('newUser')
def add_new_user(username):
    currentSocketId = request.sid
    print("Adding new user ------------------------------- ", username, currentSocketId)
    if username not in online_user:
        online_user[currentSocketId] = username

    print("0-0-0-0-0-0-0-0-0-0-0-0-0-0-00- ", online_user)


def get_reciever_id(reciever_name):
    
    # list out keys and values separately
    key_list = list(online_user.keys())
    val_list = list(online_user.values())
    
    position = val_list.index(reciever_name)
    return key_list[position]


@socketio.on('sendNotification')
def test_connect(data):
    
    currentSocketId = request.sid
    print("-------------------Notification function current socket ID : ", currentSocketId)

    senderName = data["senderName"]
    receiverName = data["receiverName"]
    type_of_notification = data["type"]

    client_id = get_reciever_id(receiverName)
    
    print("These are the sende Notification details : =----------------------- ", client_id, senderName, receiverName, type_of_notification)

    result_dict = {"senderName": senderName, "type": type_of_notification}

    emit("getNotification", (result_dict), room=client_id)

    # need visibility of the global thread object


# @socketio.on('sendText')
# def sent_text(data):
#     print("THisi isdfasdfasdfasdfasd;: ", data)
#     senderName = data["senderName"]
#     receiverName = data["receiverName"]
#     text = data["text"]

#     print("these are the notification details  --------------------- : ", senderName, receiverName, text)

#     emit("getText", (senderName, receiverName, text), broadcast=True)


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
