import requests
import pymysql
import yaml
from sqlite3 import Error
from pypika import Table, Query
from user import User
from selenium import webdriver



def rest_post(user_id,user_name):
    res = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name" : user_name})
    if res.ok:
        return {'status': 'ok', 'user_add': user_name}
    else:
        return {'status': 'error', 'reason': 'id already exits' }


def rest_get(user_id):
    res = requests.get(f"http://127.0.0.1:5000/users/{user_id}")
    if res.ok:
        return {'status': 'ok', 'user_name': res.json()['user_name']}
    else:
        return {'status': 'error', 'reason': 'no such id'}

def connect_DB():
    config = yaml.safe_load(open("config.yml"))
    connection = None
    try:
        connection = pymysql.connect(host=config['mysql']['host'],
                                     port=3306,
                                     user=config['mysql']['user'],
                                     passwd=config['mysql']['pass'],
                                     db=config['mysql']['name'])
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def unconnect_DB(cursor,connection):
    cursor.close()
    connection.close()

def get_user(user_id):
    connection = connect_DB()
    cursor = connection.cursor()
    users = Table('users')
    q = Query.from_(users).select('*').where(users.user_id == user_id)
    cursor.execute(str(q).replace('"',''))
    result = cursor.fetchall()
    unconnect_DB(cursor,connection)
    user = User(result[0]) if result else None
    print(user)
    return user if user else None


try:
    print(rest_post(2,'YOAV'))
    print(rest_get(2))
    get_user(2)
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hodaya\\Downloads\\chromedriver.exe")
    driver.get("http://127.0.0.1:5001/user/get_user_data/2")
    user = driver.find_element_by_xpath('//*[@id="user"]')
    print(user.text)
except Exception as e:
    raise Exception("test failed")
