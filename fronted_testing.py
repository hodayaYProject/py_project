from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Hodaya\\Downloads\\chromedriver.exe")
user = driver.get("http://127.0.0.1:5001/user/get_user_data/1")
print(user)