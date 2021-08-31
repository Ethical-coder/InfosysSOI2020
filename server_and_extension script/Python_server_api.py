from flask import Flask,jsonify,request
from flask_cors import CORS

import checker
app=Flask(__name__)
CORS(app)

# specifiyning the route for the post request
@app.route('/popup',methods=['POST'])
def api_response():
	#converting json object to a python object 
	data=request.get_json(force=True)
	test=checker.Tester(data['url'])
	
	message=test.fullScan()

	#sending response back to javascript
	if(message=='safe'):
		response=jsonify({'result':0,'message':message})
	else:
		response=jsonify({'result':1,'message':message})
	return response



@app.route('/content',methods=['POST'])
def response():
	#converting json object to a python object 
	data=request.get_json(force=True)
	test=checker.Tester(data['url'])

	message=test.scan()
	#sending response back to javascript
	if(message=='safe'):
		response=jsonify({'result':0,'message':message})
	else:
		response=jsonify({'result':1,'message':message})
	return response

if __name__=='__main__':
	app.run(debug=True,port=80)