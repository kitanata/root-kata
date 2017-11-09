
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

    def get_report(self):
        miles = round(self.get_total_miles_driven())

        if not miles:
            return "{name}: 0 miles".format(name=str(self))

        return "{name}: {miles} miles @ {speed} mph".format(
                             name=str(self),
                             miles=round(self.get_total_miles_driven()),
                             speed=round(self.get_average_speed()))

