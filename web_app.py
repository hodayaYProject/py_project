from flask import Flask
from db_connector import Stock
import json

app = Flask(__name__)

@app.route('/user/get_user_data/<user_id>', methods=['GET'])
def get_user_name(user_id):
    user = Stock.get_user(user_id)
    if user:
        return "<H1 id='user'>" + str(user) + "</H1>", 200
    else:
        return "<H1 id='error'> no such user: " + user_id +"</H1>", 500


app.run(host='127.0.0.1', debug=True, port=5001)