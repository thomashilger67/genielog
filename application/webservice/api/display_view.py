import re 

def count(collection,filter={}):
    return collection.count_documents(filter)


def display_home_count(collection):

    count_all=count(collection)
    count_bike=count(collection,filter={"type":"bike"})
    count_run=count(collection,filter={"type":"run"})
    count_cardio=count(collection,filter={"type":"cardio"})
    count_swim=count(collection,filter={"type":"swim"})

    html = open('application/webservice/api/templates/example.html',"r")
    resu=html.read()
    resu=re.sub(r'{{ count_tot }}',str(count_all),resu)
    resu=re.sub(r'{{ count_bike }}',str(count_bike),resu)
    resu=re.sub(r'{{ count_run }}',str(count_run),resu)
    resu=re.sub(r'{{ count_cardio }}',str(count_cardio),resu)
    resu=re.sub(r'{{ count_swim }}',str(count_swim),resu)

    return resu 

def display_data(list):
    html1="""<!DOCTYPE html>
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
    table{
        width: 100%;
        border-collapse: collapse;}
    
      
     th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;}
      </style>
      </head>
      <body>
      <div id="tableContainer"></div>
      <script>
      var data ="""
    html2=""";
      
      
      // Fonction pour générer les tableaux HTML pour chaque objet JSON
      function generateTable(data) {
        var tableContainer = document.getElementById("tableContainer");
        var table = document.createElement("table");
        
        // Pour chaque objet JSON
        for (var i = 0; i < data.length; i++) {
          var row = document.createElement("tr");
          
          // Pour chaque attribut de l'objet JSON
          for (var key in data[i]) {
            var cell = document.createElement("td");
            var cellText = document.createTextNode(key + ": " + data[i][key]);
            cell.appendChild(cellText);
            row.appendChild(cell);
          }
          
          table.appendChild(row);
        }
        
        tableContainer.appendChild(table);
      }
      
      generateTable(data);
      </script>
      </body>
      </html>
      """
    return html1 + str(list) + html2