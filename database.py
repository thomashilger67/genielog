from pymongo import MongoClient

client = MongoClient('localhost', 27017)

mydb = client["mydatabase"]

movies = mydb.movies

movie_ = {

    "title": "Mr. Robot",

    "Starring": "Rami Malek, Christian Slater, Carly Chaikin",

    "created": "Sam Esmail",

    "Year": "2016"

}

id = movies.insert_one(movie_).inserted_id

print(id)