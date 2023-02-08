

def display_update_activity(collection):
    html = open('application/webservice/api/templates/update.html',"r")
    resu=html.read()
    return resu 

def update_activity(filter,update,value_filter,value):
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



