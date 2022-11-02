from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_quotes import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/quotes')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class QuotesAPI:
    # not implemented
    class _Create(Resource):
        def post(self, quote):
            pass
            
    
    class _Read(Resource):
        def get(self):
            return jsonify(getQuotes())

    
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getQuote(id))

    
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomQuote())
    
    
    class _ReadCount(Resource):
        def get(self):
            count = countQuotes()
            countMsg = {'count': count}
            return jsonify(countMsg)

    
    class _UpdateHelp(Resource):
        def put(self, id):
            addQuoteHelp(id)
            return jsonify(getQuote(id))

    
    class _UpdateUseless(Resource):
        def put(self, id):
            addQuoteUseless(id)
            return jsonify(getQuote(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:quote>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateHelp, '/help/<int:id>')
    api.add_resource(_UpdateUseless, '/useless/<int:id>')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/quotes"
    responses = []  # responses list

    
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  
        ) 
    responses.append(
        requests.put(url+"/help/"+num) # add to like count
        ) 
    responses.append(
        requests.put(url+"/useless/"+num) # add to jeer count
        ) 

    
    responses.append(
        requests.get(url+"/random")  
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")