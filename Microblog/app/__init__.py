#从flask包中导入Flask类
from flask import Flask

app = Flask(__name__)#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。

#print('等会谁（哪个包或模块）在使用我：',__name__)

#从app包中导入模块routes
from app import routes


