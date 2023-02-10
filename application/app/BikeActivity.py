from application.app.Activity import Activity


class BikeActivity(Activity):
    """
    Activité de vélo 

    Attributs 
    --------------
    name : str nom de l'actvitié 
    time : float : durée de l'activité
    fc : int : fréquence cardiaque 
    energy : int : calories dépensées (Kcal)
    distance : float : distance parcouru (km)
    power : int : puissance moyenne durant l'activité (Watt)
    altitdue : int : dénivelé positif (m)
    
    """
    def __init__(self, name, time, fc=70, energy=0, distance=0, power= 0, altitude=0 ):
        super().__init__(name, time, fc, energy)
        self.distance= distance
        self.power=power
        self.altitude=altitude
        self.type='bike'
        
        self.set_speed

        
    def set_speed(self,display=False):
        self.speed = self.distance / (self.time /60)
        if display:

            print( "La vitesse moyenne est de {} km/h ! ".format(self.speed))
