from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():  # put application's code here
	return render_template("index.html")


# 电影详情界面
@app.route('/details_page')
def details_page():
	title = '肖申克的救赎'
	stitle = '一切的一切都要从越狱说起'
	mingju = '"向往自由，向往生活"'
	release_date = '2020-7-8'
	brife = "小女孩千寻和父母一起在森林里迷了路，走过了一条神秘的隧道之后进入了一小镇。奇怪的是整个镇子一个人也没有。千寻的父母看到有一处店铺里存放着大量新"
	img = "../static/img/肖申克.jpg"
	daoyan = "导演：宫崎骏"
	dic = {}
	dic[1] = title
	dic[2] = stitle
	dic[3] = mingju
	dic[4] = release_date
	dic[5] = brife
	dic[6] = img
	dic[7] = 999
	dic[8] = daoyan
	return render_template('details_page.html', data=dic)


# 个人主页界面
@app.route('/home_page')
def home_page():
	return render_template("home_page.html")


# 用户邀约界面
@app.route('/invite_page')
def invite_page():
	return render_template("invite_page.html")


# 聊天界面
@app.route('/chat_room')
def chat_room():
	return render_template("chat_room.html")


if __name__ == '__main__':
	app.run()
