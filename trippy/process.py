from .driver import Driver

class Processor:

    def __init__(self):
        self.drivers = []

    def __len__(self):
        return len(self.drivers)

    def _split_line(self, line):
        return tuple(line.split(' ')) # immutable

    def process_line(self, line):
        line = self._split_line(line)

        command = line[0]

        if command == "Driver":
            driver_name = line[1]
            self.drivers.append(Driver(driver_name))

    def has_driver(self, driver_name):
        return any([True if d.name == driver_name else False for d in self.drivers])

    def get_driver(self, driver_name):
        for d in self.drivers:
            if d.name == driver_name:
                return d

        return None

    def report(self):
        return ""
