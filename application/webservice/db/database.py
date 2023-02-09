from pymongo import MongoClient


def get_database():
   uri ='mongodb://db_mongo_bis:27017'
   client = MongoClient(uri)

   return client['activities']



