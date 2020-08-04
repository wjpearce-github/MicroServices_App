from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
import requests
import random



@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/rpgname')
    print(response)
    rpgname = response.text
    game_data = games.query.all()
    return render_template('index.html', rpgname=sentence, games=games_data, title='Home')
