#!/bin/env python
from app import create_app, socketio
from flask_socketio import SocketIO
app = create_app(debug="true", )



if __name__ == '__main__':

    socketio.run(app)
