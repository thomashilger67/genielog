import flask
from BikeActivity import BikeActivity



app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    bike_monday=BikeActivity(123,10,60,0)
    bike_monday.set_distance(20)

    bstr=bike_monday.display_info()
    return bike_monday.__dict__
    


app.run()   