

def display_update_activity():
    """
  fonction qui charge un template html 

  Returns : 
  -------------------------
  str : html 
  """
    html = open('application/webservice/api/templates/update.html',"r")
    resu=html.read()
    return resu 

def update_activity(filter,update,value_filter,value):
    """
  fonction qui créée le bon format pour appliquer un modification à un document mongodb 

  Parameters : 
  ------------------------
  filter : str attribut sur lequel filtrer
  update : str attribut à modifier 
  value_filter : valeur du filtre
  value : nouvele valer de l'attribut 


  Returns : 
  -------------------------
  dictionnary  
  """
    try : 
        value=float(value)
    except:
        pass
    filtre={}
    filtre[filter]=value_filter  
    new_data={}
    new_data[update]=value       
    data={"database" : "activities",
    "collection" : "user_activities", 
    "Filter": filtre,
    "DataToBeUpdated": new_data}

    return data



