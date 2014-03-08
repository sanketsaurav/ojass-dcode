from flask import Flask, render_template, abort, make_response, jsonify, Response
import string
import hashlib
import random

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
	passphrase_s = list(string.letters)
	random.shuffle(passphrase_s)
	passphrase = ''.join(passphrase_s[:13])
	return jsonify({'passphrase':passphrase, 'hash':hashlib.md5(passphrase).hexdigest()})

@app.route('/dcode2')
def dcode1():
	passphrase_s = list(string.letters)
	random.shuffle(passphrase_s)
	passphrase = ''.join(passphrase_s[:13])
	return jsonify({'passphrase':passphrase, 'hash':hashlib.md5(passphrase).hexdigest()})

@app.route('/md5')
def md5():
	r = make_response(render_template('partials/darth.html'))
	r.headers.add('s3cr3t', 'usethesourceluke')
	return r

@app.route('/dcode3')
def dcode2():
	r = make_response(render_template('partials/darth.html'))
	r.headers.add('s3cr3t', 'usethesourceluke')
	return r

@app.route('/problems')
def dcode3():
	r = make_response(render_template('partials/problem.html'))
	return r

@app.route('/usethesourceluke')
def source():
	r = make_response('UNICORNS! SERVERS! WOW!')
	return r

@app.errorhandler(404)
def incorrect(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
