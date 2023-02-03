from pymongo import MongoClient


def get_database():
 
   client = MongoClient("mongodb://172.17.0.2:27017/")

   return client['activities']


