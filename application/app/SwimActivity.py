from application.app.Activity import Activity

class SwimActivity(Activity):
    """
    Activité de natation

    Attributs 
    --------------
    name : str nom de l'actvitié 
    time : float : durée de l'activité
    fc : int : fréquence cardiaque 
    energy : int : calories dépensées (Kcal)
    distance : float : distance parcouru (km)

    
    """
    def __init__(self, name, time, fc=70, energy=0,distance=0):
        super().__init__(name, time, fc, energy)
        self.distance=distance
        self.type='swim'
   
        self.set_speed
    def set_speed(self,display=False):
        self.speed = (self.time *1000)/(self.distance*1000)
        if display:

            print( "La vitesse moyenne est de  {}min/100m!".format())