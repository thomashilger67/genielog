from application.app.Activity import Activity


class BikeActivity(Activity):
    def __init__(self, name, time, fc=70, energy=None, distance=None, power= None, altitude=None ):
        super().__init__(name, time, fc, energy)
        self.distance= distance
        self.power=power
        self.altitude=altitude
        self.type='bike'
        
        self.set_speed

        
    def set_speed(self,display=False):
        self.speed = self.distance / (self.time /60)
        if display:

            print( "the average speed is {} km/h ! ".format(self.speed))
