
class Driver:

    def __init__(self, driver_name):
        self.name = driver_name

    def __str__(self):
        return self.name

    def __len__(self):
        return 1

    def get_miles_driven(self):
        return 17.3
