from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
import requests
import random



# @app.route('/randomword', methods=['GET'])
# def sentence():
#     beginning = requests.get('http://service_2:5001/name')
#     ending = requests.get('http://service_3:5002/name')
#     response = beginning.text + "" + ending.text
#     return response

@app.route('/randomword', methods=['GET'])
def sentence():
    beginning = requests.get('http://service_2:5001/name')
    ending = requests.get('http://service_3:5002/name')
    response = "The name is" + beginning.text + "" + ending.text
    return response