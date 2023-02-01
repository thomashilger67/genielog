from Webservice.Activity import Activity

class CardioActivity(Activity):
    def __init__(self, name, time, fc=70, energy=None):
        super().__init__(name, time, fc, energy)

    def display_info(self):
        return("Your cardio activity has been taking into account!")
