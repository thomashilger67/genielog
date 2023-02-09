from application.app.Activity import Activity

class SwimActivity(Activity):
    def __init__(self, name, time, fc=70, energy=0,distance=0):
        super().__init__(name, time, fc, energy)
        self.distance=distance
        self.type='swim'
   
        self.set_speed
    def set_speed(self,display=False):
        self.speed = (self.time *1000)/(self.distance*1000)
        if display:

            print( "The average speed is {}min/100m!".format())