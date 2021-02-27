from flask import Flask
from db_connector import Stock
import json
import os
import signal

app = Flask(__name__)


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

@app.route('/user/get_user_data/<user_id>', methods=['GET'])
def get_user_name(user_id):
    user = Stock.get_user(user_id)
    if user:
        return "<h1 id='user'>" "id: " + str(user.id) + " name: " + str(user.name) + "</h1>", 200
    else:
        return "<h1 id='error'> no such user: " + user_id + "</h1>", 500


app.run(host='127.0.0.1', debug=True, port=5001)