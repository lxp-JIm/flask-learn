#从app包中导入 app这个实例
from app import app

#2个路由
@app.route('/')
@app.route('/index')
#1个视图函数
def index():
	user = {'username': 'LXP'}
	return '''
	<html>
		<head>
			<title>Home Page - Microblog</title>
		<head>
		<body>
			<h1>Hello,''' + user['username'] + '''!</h1>
		<body>
	</html>
	'''