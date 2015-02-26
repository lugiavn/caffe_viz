import os
import flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_w():
	s = ''
	s = s + "<a href=/dir?path=/> Browse </a> <br> "
	s = s + "<a href=/plot_caffe > Plot <a> <br> "
	return s

@app.route('/plot_caffe')
def plot_caffe():
	os.chdir('./tmp')
	s = '<a href=/ > Main </a> <br> '
	for id in range(0, 8):
		s = s + os.popen('/opt/caffe/tools/extra/plot_training_log.py.example ' + str(id) + ' ' + str(id) + '.png  /tmp/caffe.INFO').read()
		s = s + ' <img src=/get?path=tmp/' + str(id) + '.png /> <br> '
	os.chdir('../')
	return s 


@app.route('/get')
def get():
	return flask.send_file(flask.request.args.get('path'))

@app.route('/dir')
def dir():
	s = '<a href=/> Main </a><br> '
	s = s + 'Dir: '
	path = flask.request.args.get('path')
	p = os.path.abspath(os.path.join(path, os.pardir))
	s = s + '<a href=/dir?path=' + p + '> UUUUPPPPPP </a> <br> '
	files = os.listdir(path)
	for f in files:
		p = path + '/' + f
		if os.path.isfile(p) == False:
			s = s + '>>>>>>>>>>>>>' + '<a href=/dir?path=' + p + '>' +  f + '</a> <br> '
	s = s + 'Files:<br> '
	for f in files:
		p = path + '/' + f
		if os.path.isfile(p):
			s = s + '>>>>>>>>>>>>>' + '<a href=/get?path=' + p + '>' + f + '</a> <br> '
	return s

@app.route('/cmd')
def cmd():
	return flask.Response(os.popen(flask.request.args.get('cmd')).read(), mimetype='text/plain')


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)





