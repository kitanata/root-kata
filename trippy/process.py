from .driver import Driver

class Processor:

    def __init__(self):
        self.drivers = {}

    def __len__(self):
        return len(self.drivers)

    def _split_line(self, line):
        return tuple(line.split(' ')) # immutable

    def process_line(self, line):
        line = self._split_line(line)

        command = line[0]

        if command == "Driver":
            driver_name = line[1]

            if not self.has_driver(driver_name):
                self.drivers[driver_name] = Driver(driver_name)

    def has_driver(self, driver_name):
        return driver_name in self.drivers

    def get_driver(self, driver_name):
        return self.drivers.get(driver_name)

    def report(self):
        return ""
