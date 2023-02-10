import pytest
from application.app.BikeActivity import BikeActivity

def test_bikeactivity():
    bike_test=BikeActivity("vélo le dimanche",40,147,distance=12)
    test=[bike_test.name,bike_test.time,bike_test.distance,bike_test.fc]
    assert test == ["vélo le dimanche",40,12,147]

def test_speed(capsys):
    bike_test=BikeActivity("vélo le dimanche",60,147,distance=10)
    bike_test.set_speed(display=True)
    captured =capsys.readouterr()
    assert captured.out == "La vitesse moyenne est de 10.0 km/h ! \n"
