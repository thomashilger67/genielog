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
