#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import datetime
from flask import Flask, render_template, request, abort

app = Flask(__name__)

zulutime = datetime.datetime.now().ctime()

@app.route('/')
def hello_world():
    msg1 = '''
Hello Flask!!
%s
''' % zulutime
    return msg1

@app.route('/index')
def index_page():
    yo = {'name': 'Salva J.'}
    msg2 = render_template('index.html', url='app.salvaj.es',
        user=yo, servertime=zulutime)
    return msg2

@app.route('/form')
def form_data():
	msg3 = render_template('formulario.html', url='app.salvaj.es')
	return msg3	
	

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		return render_template("result.html", result = result)
	else:
		abort(406)	# 'Not Aceptable' error raise for GET method
	
	
if __name__ == '__main__':
    app.run(debug=True)

