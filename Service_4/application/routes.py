from application import app
import requests


@app.route('/rpgname', methods=['GET'])
def sentence():
    beginning = requests.get('http://Service_2:5001/name')
    ending = requests.get('http://Service_3:5002/name')
    response = beginning.text + " " + ending.text
    return response