from datetime import datetime

class Trip:

    def __init__(self, start_time, end_time, miles):
        self.start_time = start_time
        self.end_time = end_time
        self.miles = miles

    @classmethod
    def parse(cls, start_time, end_time, miles):
        return Trip(
            datetime.strptime(start_time, "%H:%M").time(),
            datetime.strptime(end_time, "%H:%M").time(),
            float(miles)
        )

    def get_time(self):
        hours = self.end_time.hour - self.start_time.hour
        minutes = self.end_time.minute - self.start_time.minute
        return hours * 60 + minutes

    def get_speed(self):
        return (self.miles / self.get_time()) * 60
