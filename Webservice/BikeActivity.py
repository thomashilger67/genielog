from Activity import Activity


class BikeActivity(Activity):
    def __init__(self, energy, distance, time,watt):
        super().__init__(energy, distance, time)

        self._power=watt

    def display_info(self):
        return("Your bike activity has been taking into account!")