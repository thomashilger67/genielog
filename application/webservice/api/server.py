import flask
from application.app.BikeActivity import BikeActivity
from application.app.RunActivity import RunActivity
from pymongo import MongoClient
from bson import json_util
from application.webservice.db.database import get_database
import json 
import requests
from application.webservice.api.display_view import display_home_count, display_data
from application.webservice.api.display_add import display_add_activity, create_activity,display_end
from application.webservice.api.display_update import display_update_activity, update_activity
from application.webservice.api.display_delete import display_delete_activity,delete_activity

def launch():

    db=get_database()
    collection=db["user_activities"]

    app = flask.Flask(__name__)
    app.config["DEBUG"] = True



    @app.route('/',methods=['GET'])
    def home():
      """
      endpoint de la page d'accueil

      """
      return display_home_count(collection)

            
    @app.route('/display', methods=['GET'])
    
    def display():
      """
      endpoint pour afficher l'ensemble des activitiés
      """
      items=list(collection.find())
      [item.pop("_id",None)for item in items]

      resu=display_data(items)
      print(resu)
      return resu 





    @app.route('/database',methods=['POST','PUT','DELETE'])
    def modify_database():
      """
      endpoint pour intéragir avec la base de données Mongo. 
      Les méthodes supportées : 
        -POST : ajouter une activité 
        -PUT : modifier une activité 
        -DELETE : supprimer une activité
      """    
      if flask.request.method=='POST':
          json = flask.request.json
          collection.insert_one(json)
          if flask.Response().status_code ==200:
              return "L'activité à bien été ajouté!"
          else: 
              return {"code error":flask.Response().status_code,"error": flask.Response().status}

      if flask.request.method =='PUT':
          data = flask.request.json
          collection.update_one(data["Filter"], {"$set":data["DataToBeUpdated"]})
          if flask.Response().status_code ==200:
              return "L'activité à bien été modifié!"
          else: 
              return {"code error":flask.Response().status_code,"error": flask.Response().status}


      if flask.request.method == 'DELETE':
          data=flask.request.json
          collection.delete_one(data["Filter"])
          if flask.Response().status_code ==200:
              return "L'activité à bien été supprimé!"
          else: 
              return {"code error":flask.Response().status_code,"error": flask.Response().status}






    @app.route('/update_activity',methods=['GET','POST'])  
    def get_update():
      """
      endpoint qui appelle un formulaire html pour mettre à jour une activité 
      
      """
      headers={"Content-Type": "application/json"}
      if flask.request.method == 'POST':
          filter = flask.request.form['filter']
          update = flask.request.form['update']
          filter_value = flask.request.form['filter_value']
          value=flask.request.form['value']

          data=update_activity(filter,update,filter_value,value)
          print(data)


          r=requests.put('http://localhost:5000/database',headers=headers,data=json.dumps(data))
          return display_end() + str(r.text)
      return display_update_activity()




    @app.route('/delete_activity',methods=['GET','POST'])                        
    def remove():
      """
      endpoint qui appelle un formulaire html pour supprimer une activité 

      """
      if flask.request.method == 'POST':
          headers={"Content-Type": "application/json"}
          filter = flask.request.form['filter']
          filter_value = flask.request.form['filter_value']

          data=delete_activity(filter,filter_value)

          r=requests.delete('http://localhost:5000/database',headers=headers,data=json.dumps(data))
          return display_end()+ str(r.text)
      return display_delete_activity()


    @app.route('/add_activity',methods=['GET','POST'])  
    def add_form():
      """
      endpoint qui appelle un formulaire html pour ajouter une activité 

      
      """
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
          return display_end() + str(r.text)
      
      return display_add_activity()
 
        


    app.run(host="0.0.0.0", port=5000,debug=True)

