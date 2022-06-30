from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():  # put application's code here
	return render_template("index.html")


@app.route('/detailspage')
def detailspage():
	return render_template("details_page/千与千寻.html")


if __name__ == '__main__':
	app.run()
