from application import app
import random


@app.route('/name', methods=['GET'])
def ending():

	list = ['Kong','Mac','Smith','Killer','Chomper','Biter','Samus', 'Jin', 'big']
	
	return list[random.randrange(9)]