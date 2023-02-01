import flask
from Webservice.BikeActivity import BikeActivity
from pymongo import MongoClient
from bson import json_util
from database import get_database
import json 
import requests

bike_ex1=BikeActivity(name="bike after school",time=1.5,fc=150,energy=None,distance=25,power=None,altitude=None).transforme_json()

db=get_database()
collection=db["user_activities"]

app = flask.Flask(__name__)
app.config["DEBUG"] = True






@app.route('/', methods=['GET'])
def home():


    items=collection.find()

    #return json.dumps(list(items),default=str)
    return json.loads(json_util.dumps(items))




@app.route('/add_activity',methods=['GET'])
def launch_requests():

    headers = {"Content-Type": "application/json"}
    r=requests.post('http://localhost:5000/post_json',headers=headers, data=bike_ex1)
    return r.text




@app.route('/post_json',methods=['POST'])
def add():    
    json = flask.request.json
    collection.insert_one(json)
    return "data has been recieved by server and is now stored in database!"

@app.route('/update_activity/filter=<filter>&datatoupdate=<new_data>')
def get_update(filter,new_data):
    headers={"Content-Type": "application/json"}
    data={"database" : "activities",
     "collection" : "user_activities", 
     "Filter": eval(filter),
      "DataToBeUpdated": eval(new_data)}


    r=requests.put('http://localhost:5000/update',headers=headers,data=json.dumps(data))
    return r.text
@app.route('/update', methods=['PUT'])
def mongo_update():
    
    data = flask.request.json
    collection.update_one(data["Filter"], {"$set":data["DataToBeUpdated"]})
    return "the activity has been updated!"

app.run()   


