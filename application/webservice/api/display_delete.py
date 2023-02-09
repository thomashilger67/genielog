def display_delete_activity():
    """
  fonction qui charge un template html 

  Returns : 
  -------------------------
  str : html 
  """
    html = open('application/webservice/api/templates/remove.html',"r")
    resu=html.read()
    return resu 

    
def delete_activity(filter,value_filter):
    """
  fonction qui créée le bon format pour appliquer une suppression de document mongodb 

  Parameters : 
  ------------------------
  filter : str attribut sur lequel filtrer
  value_filter : valeur du filtre


  Returns : 
  -------------------------
  dictionnary  
  """
    filtre={}
    filtre[filter]=value_filter  
     
    data={"database" : "activities",
    "collection" : "user_activities", 
    "Filter": filtre}

    return data