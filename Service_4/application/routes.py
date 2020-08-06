from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
import requests
import random

app.config['SECRET_KEY'] = '60ae1c92bc03176e8976331683eb9c54' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)

class games(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    f_name = db.Column(db.String(50), nullable=False)
   
    def __repr__(self):
        return ''.join(
        [
            'F_name: ' + self.f_name + '\n' 
            'ID: ' + str(self.id)
        ]
    )




@app.route('/merge', methods=['GET', 'POST'])
def merge():
    first_name = requests.get('http://service_2:5001/name').text
    second_name = requests.get('http://service_3:5002/name').text
    response = "Rpg Name: " + str(first_name) + str(second_name)
    game_data = games(
            first_names=str(first_name),
            second_names=str(second_name)
        )
    db.session.add(game_data)
    db.session.commit()
    return response





