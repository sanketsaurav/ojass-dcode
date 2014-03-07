from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('home.html')

@app.route('/<secret>')
def success(secret):

	try:
		return render_template('partials/%s.html' % secret)
	except:
		return abort(404)

@app.errorhandler(404)
def incorrect(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)