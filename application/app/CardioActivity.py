from application.app.Activity import Activity

class CardioActivity(Activity):
    """
    Activité de cardio 

    Attributs 
    --------------
    name : str nom de l'actvitié 
    time : float : durée de l'activité
    fc : int : fréquence cardiaque 
    energy : int : calories dépensées (Kcal)


    """
    def __init__(self, name, time, fc=70, energy=0):
        super().__init__(name, time, fc, energy)
        self.type='cardio'
    def set_speed(self,display=False):
        
        raise Exception("Il n'y a pas de vitesse pour cette activité!")