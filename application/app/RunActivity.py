from application.app.Activity import Activity
import math

class RunActivity(Activity):
    def __init__(self, name, time, fc=70, energy=0,distance=0, cadence=0):
        super().__init__(name, time, fc, energy)
        self.distance=distance
        self.cadence=cadence
        self.type='run'
        self.set_speed()

    def set_speed(self,display=False):
        speed = self.time /self.distance
        deci_speed = (speed - math.floor(speed))*60
        self.speed = round(math.floor(speed)+ (deci_speed/100),2)

        if display : 

            print("the average speed is {} min/km !".format(self.speed))

