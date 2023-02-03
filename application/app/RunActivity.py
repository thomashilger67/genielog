from application.app.Activity import Activity


class RunActivity(Activity):
    def __init__(self, name, time, fc=70, energy=None,distance=None, cadence=None):
        super().__init__(name, time, fc, energy)
        self.distance=distance
        self.cadence=cadence
        self.speed=self.time/self.distance 
        self.type='run'
    def display_info(self):
        return("Your run activity has been taking into account!")
