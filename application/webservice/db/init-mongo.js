db = new Mongo().getDB("activities");

db.createCollection('user_activities', { autoIndexId: false });

db.user_activities.insertOne(
    {
        "name": "bike after diner",
        "time": 1.5,
        "fc": 150,
        "energy": 850,
        "date": "2023-02-03 10:17:00",
        "distance": 25,
        "speed": 16.666666666666668,
        "type" : "Bike",
        "power": 0,
        "altitude": 0,
        
      });
