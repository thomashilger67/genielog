from pymongo import MongoClient
from Webservice.BikeActivity import BikeActivity
from Webservice.RunActivity import RunActivity

bike_ex1=BikeActivity(120,10,60,500,"bike activity")
run_ex1=RunActivity(800,15,50,20,"run activity")

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   client = MongoClient("mongodb://localhost:27017/")

   # Create the database for our example (we will use the same database throughout the tutorial
   return client['activities']


db=get_database()
collection=db["user_activities"]

act1=bike_ex1.transforme_json()
act2=run_ex1.transforme_json()

#collection.insert_many([act1,act2])

item_details = collection.find()
for item in item_details:
   # This does not give a very readable output
   print(item)
