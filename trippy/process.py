from .driver import Driver
from .trip import Trip

class Processor:

    def __init__(self):
        self._drivers = {}

    def __len__(self):
        return len(self._drivers)

    def _split_line(self, line):
        return tuple(line.split(' ')) # immutable

    def process_line(self, line):
        line = self._split_line(line)
        line = [item.strip() for item in line]

        command = line[0]

        if command == "Driver":
            driver_name = line[1]

            if not self.has_driver(driver_name):
                self._drivers[driver_name] = Driver(driver_name)

        elif command == "Trip":
            driver_name = line[1]
            start_time = line[2]
            end_time = line[3]
            miles = line[4]

            driver = self.get_driver(driver_name)

            if driver is None:
                return

            trip = Trip.parse(start_time, end_time, miles)

            if trip.get_speed() > 100:
                return

            if trip.get_speed() < 5:
                return

            driver.add_trip(trip)

    def has_driver(self, driver_name):
        return driver_name in self._drivers

    def get_driver(self, driver_name):
        return self._drivers.get(driver_name)

    def get_report(self):
        drivers = sorted(self._drivers.values(), 
                         key=lambda x: x.get_total_miles_driven(), 
                         reverse=True)

        return [d.get_report() for d in drivers]
