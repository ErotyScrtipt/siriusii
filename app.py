from flask import Flask, render_template, request
from main import *
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = check(text.lower())
    return render_template('index.html', text_out=processed_text)
