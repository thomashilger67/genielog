def display_delete_activity(collection):
    html = open('application/webservice/api/templates/remove.html',"r")
    resu=html.read()
    return resu 

    
def delete_activity(filter,value_filter):
    filtre={}
    filtre[filter]=value_filter  
     
    data={"database" : "activities",
    "collection" : "user_activities", 
    "Filter": filtre}

    return data