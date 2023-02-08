import flask
from application.app.BikeActivity import BikeActivity
from application.app.RunActivity import RunActivity
from pymongo import MongoClient
from bson import json_util
from application.webservice.db.database import get_database
import json 
import requests
from application.webservice.api.display_view import display_home_count
from application.webservice.api.display_add import display_add_activity, create_activity,display_end
from application.webservice.api.display_update import display_update_activity, update_activity
from application.webservice.api.display_delete import display_delete_activity,delete_activity
import re 
html="""<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Sport Tracker</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="http://localhost:5000/">Sport Tracker</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="http://localhost:5000">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:5000/display">afficher les activités</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:5000/add_activity">Ajouter une activité</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:5000/update_activity">modifier une activité </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:5000/delete_activity">supprimer une activité</a>
          </li>
        </ul>
      </div>
    </nav>
    <style>
    table{{
        width: 100%;
        border-collapse: collapse;}}
    
      
     th, td {{
        border: 1px solid black;
        padding: 8px;
        text-align: left;}}
      </style>
      </head>
      <body>
      <div id="tableContainer"></div>
      <script>
      var data = {code};
      
      // Fonction pour générer les tableaux HTML pour chaque objet JSON
      function generateTable(data) {{
        var tableContainer = document.getElementById("tableContainer");
        var table = document.createElement("table");
        
        // Pour chaque objet JSON
        for (var i = 0; i < data.length; i++) {{
          var row = document.createElement("tr");
          
          // Pour chaque attribut de l'objet JSON
          for (var key in data[i]) {{
            var cell = document.createElement("td");
            var cellText = document.createTextNode(key + ": " + data[i][key]);
            cell.appendChild(cellText);
            row.appendChild(cell);
          }}
          
          table.appendChild(row);
        }}
        
        tableContainer.appendChild(table);
      }}
      
      generateTable(data);
      </script>
      </body>
      </html>
      """
def launch():

    db=get_database()
    collection=db["user_activities"]

    app = flask.Flask(__name__)
    app.config["DEBUG"] = True



    @app.route('/',methods=['GET'])
    def home():
        
        return display_home_count(collection)

            
    @app.route('/display', methods=['GET'])
    def display():
        items=collection.find()
        #html = open('application/webservice/api/templates/display.html',"r")
        #resu=html.read()
        #print(list(items))
        resu=html.format(code=list(items))
        print(resu)
        return resu 





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






    @app.route('/update_activity',methods=['GET','POST'])  
    def get_update():
        headers={"Content-Type": "application/json"}
        if flask.request.method == 'POST':
            filter = flask.request.form['filter']
            update = flask.request.form['update']
            filter_value = flask.request.form['filter_value']
            value=flask.request.form['value']

            data=update_activity(filter,update,filter_value,value)
            print(data)


            r=requests.put('http://localhost:5000/database',headers=headers,data=json.dumps(data))
            return display_end() + "L'activité à bien été modifié ! "
        return display_update_activity(collection)




    @app.route('/delete_activity',methods=['GET','POST'])                        
    def remove():
        if flask.request.method == 'POST':
            headers={"Content-Type": "application/json"}
            filter = flask.request.form['filter']
            filter_value = flask.request.form['filter_value']

            data=delete_activity(filter,filter_value)

            r=requests.delete('http://localhost:5000/database',headers=headers,data=json.dumps(data))
            return display_end()+ "L'activité a bien été supprimé !"
        return display_delete_activity(collection)


    @app.route('/add_activity',methods=['GET','POST'])  
    def add_form():
        if flask.request.method == 'POST':
            type = flask.request.form['activity']
            nom = flask.request.form['nom']
            time = float(flask.request.form['time'])
            energy=float(flask.request.form['energy'])
            distance = float(flask.request.form['distance'])
            fc = float(flask.request.form['fc'])
            power = int(flask.request.form['power'])
            altitude=float(flask.request.form['altitude'])
            cadence=float(flask.request.form['cadence'])

            act=create_activity(type,nom,time,fc,energy,distance,power,altitude,cadence)

            headers = {"Content-Type": "application/json"}
            r=requests.post('http://localhost:5000/database',headers=headers, data=act)
            return display_end() + "L'activité à bien été ajouté ! "
        
        return display_add_activity(collection)
 
        


    app.run(debug=True)

