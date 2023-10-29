from DrissionPage import ChromiumPage
import os
import socket
import json
# from DrissionPage.easy_set import set_paths

# set_paths(browser_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')

page = ChromiumPage()
page.get('http://10.23.2.4')
page.ele('#toLogOut').click(by_js=True)
page.ele('#sure').click(by_js=True,timeout=2)

page.quit()