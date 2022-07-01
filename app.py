import json
import houduan
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/gerenzhongxin',methods=['POST','GET'])
def index():
    data = houduan.data
    yaoyue = houduan.yaoyue
    return render_template("personal2.html",data=data,yaoyue=yaoyue,friend=houduan.dic)

# 修改信息的路由
@app.route('/xiugaixinxi',methods=['POST'])
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
    flag='修改成功'
    flag = json.dumps(flag, ensure_ascii=False)
    return flag

# 修改密码的路由
@app.route('/xiugaimima',methods=['POST'])
def xiugaimima():

    xinmima=request.form.get('xinmima')
    houduan.data['password']=xinmima
    flag='修改成功'
    return flag

@app.route('/')
def hello():
    return "hello_world"


if __name__ == '__main__':
    app.run()
