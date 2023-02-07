from abc import ABC, abstractmethod
from bson import json_util
import json 
from datetime import datetime
from fastapi.encoders import jsonable_encoder

class Activity(ABC):
    def __init__(self,name,time,fc=70,energy=None):
        self.name=name
        self.time=time
        self.fc=fc
        if energy is None:
            self.energy = ((fc /200)-0.25)*1700
        else : 
            self.energy=energy
        
        self.date=now = datetime.now().replace(second=0, microsecond=0)

        

    @abstractmethod
    def set_speed(self,display=False):
        pass 

    def transforme_json(self):
        return json.dumps(self.__dict__,default=str)

    

        
