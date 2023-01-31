from Activity import Activity


class RunActivity(Activity):
    def __init__(self, energy, distance, time,speed,name):
        super().__init__(name, time)

        self._energy=energy
        self._distance=distance
        self._speed=speed

    def display_info(self):
        return("Your run activity has been taking into account!")
