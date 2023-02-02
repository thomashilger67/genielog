from pymongo import MongoClient
from Webservice.BikeActivity import BikeActivity
from Webservice.RunActivity import RunActivity


def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   client = MongoClient("mongodb://172.17.0.2:27017/")

   # Create the database for our example (we will use the same database throughout the tutorial
   return client['activities']


#collection.insert_many([act1,act2])

