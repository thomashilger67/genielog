from Webservice.Activity import Activity

class SwimActivity(Activity):
    def __init__(self, name, time, fc=70, energy=None,distance=None):
        super().__init__(name, time, fc, energy)
        self.distance=distance
        self.speed=self.time/self.distance

    def display_info(self):
        return("Your swim activity has been taking into account!")
