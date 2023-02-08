import re 
from application.app.BikeActivity import BikeActivity
from application.app.RunActivity import RunActivity
from application.app.SwimActivity import SwimActivity
from application.app.CardioActivity import CardioActivity

def display_add_activity(collection):
    html = open('application/webservice/api/templates/form.html',"r")
    resu=html.read()
    return resu 
def create_activity(type,nom,time,fc,energy,distance,power,altitude,cadence):
    if type =='Bike':
        return BikeActivity(nom,time,fc,energy,distance,power,altitude).transforme_json()
    if type =='Run':
        return RunActivity(nom,time,fc,energy,distance,cadence).transforme_json()
    if type =='Cardio':
        return CardioActivity(nom,time,fc,energy).transforme_json()
    else :
        return SwimActivity(nom,time,fc,energy,distance).transforme_json()

def display_end():
    return """<html>
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
            <a class="nav-link" href="http://localhost:5000/display">modifier une activité </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:5000/display">supprimer une activité</a>
          </li>
        </ul>
      </div>
    </nav>
   
    """