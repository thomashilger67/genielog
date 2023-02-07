db = new Mongo().getDB("activities");

db.createCollection('user_activities');

db.user_activities.insertOne(
    {
        "_id": {
          "oid": "63dcd1457c2ddfe0fb69e19d"
        },
        "name": "bike after diner",
        "time": 1.5,
        "fc": 150,
        "energy": 850,
        "date": "2023-02-03 10:17:00",
        "distance": 25,
        "power": null,
        "altitude": null,
        "speed": 16.666666666666668
      });
