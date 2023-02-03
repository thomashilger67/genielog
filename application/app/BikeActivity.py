from application.app.Activity import Activity


class BikeActivity(Activity):
    def __init__(self, name, time, fc=70, energy=None, distance=None, power= None, altitude=None ):
        super().__init__(name, time, fc, energy)
        self.distance= distance
        self.power=power
        self.altitude=altitude

        self.speed=distance/time
        
    def display_info(self):
        return("Your bike activity has been taking into account!")