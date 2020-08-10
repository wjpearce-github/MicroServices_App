from application import app
import random



@app.route('/name', methods=['GET'])
def beginning():

	list = ['Kirby','Rapid','Luigui','Mario','Tiny','Fire','John', 'Samus']
	# 	list = ['Link','Fast','Tall','Bowser','Small','Big','Wizard', 'Angry']
	
	return list[random.randrange(8)]