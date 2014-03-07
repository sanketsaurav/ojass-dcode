from flask import Flask, render_template, abort, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('home.html')

@app.route('/42')
def forty_two():
	r = make_response(render_template('partials/42.html'))
	r.set_cookie('s3cr3t', '1337')
	return r

@app.route('/1337')
def leet():
	r = make_response(render_template('partials/leet.html'))
	r.set_cookie('s3cr3t', '')
	return r

@app.route('/xkcd')
def xkcd():
	return jsonify({'passphrase':'wWcjszQquamGk', 'hash':'d4c51be4152a53795497f13ff28d60b9'})

@app.route('/md5')
def md5():
	pass

@app.errorhandler(404)
def incorrect(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
