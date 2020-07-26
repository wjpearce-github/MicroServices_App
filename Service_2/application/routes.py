from application import app
import random


@app.route('/name', methods=['GET'])
def beginning():

	list = ['Link','Jim','John','Bowser','How are','Luigi','Kirby ']
	
	return list[random.randrange(6)]