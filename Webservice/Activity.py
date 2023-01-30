from abc import ABC, abstractmethod


class Activity(ABC):
    def __init__(self,energy,distance,time):
        self._energy=energy
        self._distance=distance
        self._time=time

    def set_energy(self,energy):
        self._energy=energy

    def set_distance(self,distance):
        self._distance=distance

    def set_time(self,time):
        self._time=time


    @abstractmethod
    def display_info(self):
        pass 