确保电脑上有Chrome浏览器，在安装所需要的库
`pip install -r requirements.txt`
如使用Edge浏览器，在运行前运行
```
from DrissionPage.easy_set import set_paths
set_paths(browser_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
```
设置默认浏览器为Edge浏览器

1. 请在电脑有网的情况下运行一次`con_net.bat`，输入正确的账号和密码
2. 运行`断开网络.bat`再次运行`con_net.bat`进行测试网络连接
3. 测试成功后打开任务计划程序进行设置定时启动或其他启动方式，启动程序为`con_net.bat`
