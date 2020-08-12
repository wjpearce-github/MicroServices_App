from application import app
import random


@app.route('/name', methods=['GET'])
def ending():

	list = ['Kong','Mac','Smith','Killer','Chomper','Biter','Samus', 'Jin']
	#list = ['Kirby','Will','Heavy','King','Stinker','Tanky','Fire', 'Small']
	
	return list[random.randrange(8)]