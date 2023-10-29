from DrissionPage import ChromiumPage
import os
import socket
import json

# from DrissionPage.easy_set import set_paths
# set_paths(browser_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

# 指定文件名
filename = '账号.json'

def is_connected():
    try:
        # 使用Google的DNS服务器进行测试
        socket.create_connection(('8.8.8.8', 53), timeout=0.5)
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


    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({}, f)

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key in ('账号', '密码','网络运营商（电信1，移动2，联通3）'):
        if key not in data or not data[key]:
            data[key] = input("请输入{}：".format(key))

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)
else:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        page = ChromiumPage()
        page.get('http://10.23.2.4')
        # time.sleep(0.2)
        ele = page.ele('username').input(data['账号'],)
        ele = page.ele('@value=密码').input(data['密码'])
        ele = page.ele('#xiala').click(by_js=True)
        # ele = Keys.ENTER
        # ele = page.ele('selectDisname').click
        server = data['网络运营商（电信1，移动2，联通3）']
        if server == '1':
            ele = page.ele('#_service_1').click(by_js=True)
        elif server == '2':
            ele = page.ele('#_service_2').click(by_js=True) # 电信1，移动2，联通3
        elif server == '3':
            ele = page.ele('#_service_3').click(by_js=True)
        ele = page.ele('#loginLink_div').click(by_js=True)
        page.quit()
    
    
    


