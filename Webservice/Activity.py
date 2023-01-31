from abc import ABC, abstractmethod


class Activity(ABC):
    def __init__(self,name,time):
        self._time=time
        self._name=name


    def set_time(self,time):
        self._time=time


    @abstractmethod
    def display_info(self):
        pass 

    def transforme_json(self):
        return self.__dict__