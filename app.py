from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():  # put application's code here
	return render_template("index.html")

# 电影详情界面
@app.route('/details_page')
def details_page():
	return render_template("details_page/千与千寻.html")
	# return render_template("details_page/教父.html")
	# return render_template("details_page/爱乐之城.html")

# 个人主页界面
@app.route('/home_page')
def home_page():
	return render_template("home_page.html")

# 用户邀约界面
# @app.route('/home_page')
# def home_page():
# 	return render_template("home_page.html")

# 聊天界面
# @app.route('/home_page')
# def home_page():
# 	return render_template("home_page.html")





if __name__ == '__main__':
	app.run()
