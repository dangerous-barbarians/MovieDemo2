import json
from flask import Flask, render_template, request
import houduan

app = Flask(__name__, template_folder='templates')

# 主页
@app.route('/')
def index():  # put application's code here
	return render_template("index.html")


# 电影详情界面
@app.route('/details_page',methods=['POST','GET'])
def details_page():
	title = '肖申克的救赎'
	stitle = '一切的一切都要从越狱说起'
	mingju = '"向往自由，向往生活"'
	release_date = '2020-7-8'
	brife = "小女孩千寻和父母一起在森林里迷了路，走过了一条神秘的隧道之后进入了一小镇。奇怪的是整个镇子一个人也没有。千寻的父母看到有一处店铺里存放着大量新"
	img = "../static/img/1.jpg"
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


# 用户邀约界面
@app.route('/invite_page')
def invite_page():
	return render_template("invite_page.html")


# 聊天界面
@app.route('/chat_room')
def chat_room():
	return render_template("chat_room.html")

# 个人主页界面
@app.route('/home_page', methods=['POST', 'GET'])
def home_page():
	data = houduan.data
	yaoyue = houduan.yaoyue
	return render_template("home_page.html", data=data, yaoyue=yaoyue, friend=houduan.dic)

# 修改信息的路由
@app.route('/xiugaixinxi', methods=['POST'])
def xiugaixinxi():
	head_portrait = request.form.get('head_portrait')
	gender = request.form.get('gender')
	age = request.form.get('age')
	self_introduction = request.form.get('self_introduction')
	current_address = request.form.get('current_address')
	phone_number = request.form.get('phone_number')
	if age != "":
		houduan.data['age'] = age
	if gender != "":
		houduan.data['sex'] = gender
	if phone_number != "":
		houduan.data['phone'] = phone_number
	if current_address != "":
		houduan.data['adderss'] = current_address
	if head_portrait != "":
		houduan.data['touxiang'] = head_portrait
	if self_introduction != "":
		houduan.data['breif'] = self_introduction
	flag = '修改成功'
	flag = json.dumps(flag, ensure_ascii=False)
	return flag

# 修改密码的路由
@app.route('/xiugaimima', methods=['POST'])
def xiugaimima():
	xinmima = request.form.get('xinmima')
	houduan.data['password'] = xinmima
	flag = '修改成功'
	return flag

# 登录界面
@app.route('/login',methods=['POST','GET'])
def login():
	return render_template("login.html")

# 验证登陆的路由
@app.route('/denglupanduan',methods=['POST','GET'])
def login_judge():
	flag = '1'
	print(1)
	return flag

# 注册界面
@app.route('/register',methods=['POST','GET'])
def register():
	print('1')
	return render_template('register.html')

# 验证注册的路由
@app.route('/zhucepanduan',methods=['POST','GET'])
def register_judge():
	registerUsername = request.form.get('registerUsername')
	print(registerUsername)
	print('1')
	flag = '1'
	return flag


@app.route('/fly',methods=['POST','GET'])
def fly():
	return render_template('fly.html')


if __name__ == '__main__':
	app.run()
