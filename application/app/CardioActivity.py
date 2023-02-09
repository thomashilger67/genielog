from application.app.Activity import Activity

class CardioActivity(Activity):
    def __init__(self, name, time, fc=70, energy=0):
        super().__init__(name, time, fc, energy)
        self.type='cardio'
    def set_speed(self,display=False):
        
        raise Exception("You can't compute a speed for a cardio actvitiy")