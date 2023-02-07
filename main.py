import flask
from application.app.BikeActivity import BikeActivity
from pymongo import MongoClient
from bson import json_util
from application.webservice.db.database import get_database
import json 
import requests

bike_ex1=BikeActivity(name="bike after the noon",time=1.5,fc=150,energy=None,distance=25,power=None,altitude=None).transforme_json()

db=get_database()
collection=db["user_activities"]

app = flask.Flask(__name__)
app.config["DEBUG"] = True




@app.route('/', methods=['GET'])
def home():


    items=collection.find()

    return json.loads(json_util.dumps(items))




@app.route('/database',methods=['POST','PUT','DELETE'])
def modify_database():    
    if flask.request.method=='POST':
        json = flask.request.json
        collection.insert_one(json)
        if flask.Response().status_code ==200:
            return "data has been recieved by server and is now stored in database!"
        else: 
            return {"code error":flask.Response().status_code,"error": flask.Response().status}

    if flask.request.method =='PUT':
        data = flask.request.json
        collection.update_one(data["Filter"], {"$set":data["DataToBeUpdated"]})
        if flask.Response().status_code ==200:
            return "the activity has been updated!"
        else: 
            return {"code error":flask.Response().status_code,"error": flask.Response().status}


    if flask.request.method == 'DELETE':
        data=flask.request.json
        collection.delete_one(data["Filter"])
        if flask.Response().status_code ==200:
            return "the activity has been deleted!"
        else: 
            return {"code error":flask.Response().status_code,"error": flask.Response().status}





@app.route('/add_activity',methods=['GET'])                             #méthode temporaire 
def launch_requests():

    headers = {"Content-Type": "application/json"}
    r=requests.post('http://localhost:5000/database',headers=headers, data=bike_ex1)
    return r.text



@app.route('/update_activity/filter=<filter>&datatoupdate=<new_data>',methods=['GET'])   #méthode temporaire 
def get_update(filter,new_data):
    headers={"Content-Type": "application/json"}
    data={"database" : "activities",
     "collection" : "user_activities", 
     "Filter": eval(filter),
      "DataToBeUpdated": eval(new_data)}


    r=requests.put('http://localhost:5000/database',headers=headers,data=json.dumps(data))
    return r.text



@app.route('/remove_activity/filter=<filter>',methods=['GET'])                          # methode temporaire 
def remove(filter):
    headers={"Content-Type": "application/json"}
    data={"database" : "activities",
     "collection" : "user_activities", 
     "Filter": eval(filter)}


    r=requests.delete('http://localhost:5000/database',headers=headers,data=json.dumps(data))
    return r.text


if __name__ == "__main__":
    app.run(debug=True)