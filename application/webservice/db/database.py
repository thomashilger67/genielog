from pymongo import MongoClient


def get_database():
   uri ='mongodb://localhost:27017'
   client = MongoClient(uri)

   return client['activities']


