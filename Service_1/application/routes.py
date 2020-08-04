from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
import requests
import os
import random



@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    print(response)
    game = response.text
    game_data = games(
        f_name=game
        
    )
    games_data = games.query.order_by(games.id.desc())
    db.session.add(game_data)
    db.session.commit()
    return render_template('index.html', game = game, games_data = games_data, title = 'Home')


