# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import os
# import socket
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# NETWORK_IP = "10.23.2.4"  # Update this with the appropriate IP address

# # 获取当前工作目录
# current_directory = os.getcwd()
# # 打印当前工作目录
# # print("当前工作目录是: ", current_directory)
# # 文件绝对路径
# current_file_path = __file__
# # 借助dirname()从绝对路径中提取目录
# current_file_dir = os.path.dirname(current_file_path)
# os.chdir(current_file_dir)
# # 获取当前工作目录
# current_directory = os.getcwd()
# # 打印当前工作目录
# # print("当前工作目录是: ", current_directory)


# def is_connected():
#     try:
#         # use Google's DNS server for testing connectivity
#         socket.create_connection(('8.8.8.8', 53), timeout=2)
#         return True
#     except OSError:
#         pass
#     return False


# if is_connected():
#     print("Disconnecting network...")
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     service = Service(ChromeDriverManager(path=r".\\Drivers").install())
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.get(f"http://{NETWORK_IP}")
#     time.sleep(1)
#     driver.find_element(By.ID, 'toLogOut').click()
#     time.sleep(0.1)
#     driver.find_element(By.ID, 'sure').click()
#     driver.quit()
#     if not is_connected():
#         print("Network disconnected.")
#     else:
#         print("Failed to disconnect network.")
# else:
#     print("Not connected to network.")
import os
import socket
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


NETWORK_IP = "10.23.2.4"
current_file_path = __file__
current_file_dir = os.path.dirname(os.path.abspath(current_file_path))
os.chdir(current_file_dir)


def is_connected():
    try:
        socket.create_connection(('8.8.8.8', 53), timeout=0.1)
        return True
    except OSError:
        pass
    return False


if is_connected():
    print("Disconnecting network...")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(ChromeDriverManager(path=os.path.join(current_file_dir, 'Drivers')).install())
    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get(f"http://{NETWORK_IP}")
        time.sleep(1)
        driver.find_element(By.ID, 'toLogOut').click()
        time.sleep(0.1)
        driver.find_element(By.ID, 'sure').click()
    if not is_connected():
        print("Network disconnected.")
    else:
        print("Failed to disconnect network.")
else:
    print("Not connected to network.")
