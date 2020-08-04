from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
import requests
import os
import random

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/rpgname')
    rpgname = response.text
    return render_template('index.html', rpgname = rpgname, title = 'Home')
