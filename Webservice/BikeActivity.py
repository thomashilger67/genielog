from Webservice.Activity import Activity


class BikeActivity(Activity):
    def __init__(self, energy, distance, time,watt,name):
        super().__init__(name, time)

        self._energy=energy
        self._distance=distance
        self._power=watt

    def display_info(self):
        return("Your bike activity has been taking into account!")