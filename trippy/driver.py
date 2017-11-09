
class Driver:

    def __init__(self, driver_name):
        self.name = driver_name
        self._trips = []

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self._trips)

    def add_trip(self, trip):
        self._trips.append(trip)

    def get_total_miles_driven(self):
        return sum([t.miles for t in self._trips])

    def get_average_speed(self):
        if not len(self):
            return 0

        total_miles = sum([t.miles for t in self._trips])
        total_time = sum([t.get_time() for t in self._trips])

        return (total_miles / total_time) * 60

