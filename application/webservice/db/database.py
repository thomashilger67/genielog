from pymongo import MongoClient


def get_database():
   """
   connection à la base de données MongoDB 
   uri : mongodb://db_mongo_bis:27017
   """
   uri ='mongodb://db_mongo_bis:27017'
   client = MongoClient(uri)

   return client['activities']



