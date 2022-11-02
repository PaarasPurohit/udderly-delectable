# import "packages" from flask
from flask import Flask, render_template, abort, url_for, json, jsonify, request
import json
import html
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition
import requests

app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/app/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("app.html")

@app.route('/api/quotes',methods=["GET","POST"])  # connects /stub/ URL to stub() function
def api_quotes():
    # GET request
    if request.method =="GET":
        method= 'POST'
        url= 'https://motivational-quotes1.p.rapidapi.com/motivation'
        headers = {
            'content-type': 'application/json',
            'X-RapidAPI-Key': '6615470177msh2eb9d9776c82332p163317jsn65585d1a22d9',
            'X-RapidAPI-Host': 'motivational-quotes1.p.rapidapi.com'
        }
        data = '{"key1":"value","key2":"value"}'
        responses={}
        for i in range(100):
            response = requests.request(method, url, headers=headers, data=data)
            print(response.text)
            text=response.text
            responses[text]=text
            # End Rapid API Code
        responsesJson = json.dumps(responses)
        print(responsesJson)
        return(responsesJson)
    
    # POST request
    if request.method=="POST":
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/chart/')
def chart():
    return render_template("chart.html")

# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
