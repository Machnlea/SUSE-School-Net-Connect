import json
import os
import socket
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# 指定文件名
filename = '账号.json'


def is_connected():
    try:
        # 使用Google的DNS服务器进行测试
        socket.create_connection(('8.8.8.8', 53), timeout=0.1)
        return True
    except OSError:
        pass
    return False


# 获取当前脚本所在路径
script_dir = os.path.abspath(__file__)
# 切换到该路径下
os.chdir(os.path.dirname(script_dir))

if is_connected():
    print("已连接网络")
    ChromeDriverManager(path=r".\\Drivers").install()

    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({}, f)

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key in ('账号', '密码'):
        if key not in data or not data[key]:
            data[key] = input("请输入{}：".format(key))

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

else:
    # 获取 Chrome 浏览器二进制文件路径
    with open('.\\Drivers\\.wdm\\drivers.json', 'r') as f:
        data = json.load(f)

    binary_path = list(data.values())[-1]['binary_path']

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(binary_path)
    browser = webdriver.Chrome(service=service, options=options)

    print("开始连接网络")
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    browser.get('http://10.23.2.4')
    time.sleep(0.2)
    browser.find_element(By.XPATH, '//*[@id="username"]') \
        .send_keys(data['账号'], Keys.ENTER, data['密码'])
    time.sleep(0.1)
    browser.find_element(By.ID, 'xiala').click()
    time.sleep(0.1)
    browser.find_element(By.ID, '_service_2').click()
    time.sleep(0.1)
    browser.find_element(By.ID, 'loginLink_div').click()
    browser.quit()

    if is_connected():
        print("已连接网络")
