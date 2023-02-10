from abc import ABC, abstractmethod
from bson import json_util
import json 
from datetime import datetime
from fastapi.encoders import jsonable_encoder

class Activity(ABC):
    """
    classe abstraite pour représenter une activité sportive 
    
    """
    def __init__(self,name,time,fc=70,energy=0):
        self.name=name
        self.time=time
        self.fc=fc
        if energy==0:
            self.energy = ((fc /200)-0.25)*1700
        else : 
            self.energy=energy
        
        self.date=now = datetime.now().replace(second=0, microsecond=0)

        

    @abstractmethod
    def set_speed(self,display=False):
        pass 

    def transforme_json(self):
        """
        Transforme notre objet Activity en un format json 
        """
        return json.dumps(self.__dict__,default=str)

    

        
