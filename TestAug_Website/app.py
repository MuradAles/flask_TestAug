# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:37:07 2022

@author: RedRo
"""

import os
import sys


#from testAug import ...


from flask import Flask, render_template, redirect, url_for, request

#os.environ["PYTHONUNBUFFERED"] = "TRUE"

app = Flask(__name__)

#replace with global reference to object
data = ""

#FUNCTIONS
def modifyOutput(text):
    return text*3

#ROUTES

#On first connection to the website you can try to 'initialize' variables here
@app.route('/')
def index():
    # This forces a printline
#    print("DEFAULT", flush=True)
    global data
    data = "example: "
    return redirect(url_for('_input'))
                           
#Initial App Routing
@app.route('/input',methods=['GET','POST'])
def _input():    
    app.logger.info("Form method: " + request.method)
    sys.stdout.flush()
    if request.method == 'POST':
#       Can process the input information here        
        userInput = modifyOutput(request.form['text'])
        return redirect(url_for('dynamic', text=userInput))
    else:
        return render_template('input.html')

#Response from User Input, can be used to handle 'dialogue'
@app.route('/dynamic/<text>',methods=['GET','POST'])
def dynamic(text):
    global data
    app.logger.info(text)
    if request.method == 'POST':
        userInput = modifyOutput(request.form['text'])
        return redirect(url_for('dynamic', text=userInput))
    else:
        return render_template('dynamic.html',processedInput=text)

#TODO: make CSS for output

if __name__ == '__main__':
    app.run(debug=True)