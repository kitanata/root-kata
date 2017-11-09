import sure
import datetime

from trippy.trip import Trip

def test_parse_trip():
    trip = Trip.parse("07:15", "07:45", "17.3")

    trip.start_time.should.equal(datetime.time(hour=7, minute=15))
    trip.end_time.should.equal(datetime.time(hour=7, minute=45))
    trip.miles.should.equal(17.3)

def test_get_trip_time():
    trip = Trip.parse("07:15", "07:45", "17.3")
    trip_time = trip.get_time()
    trip_time.should.equal(30)

def test_get_trip_time_cross_hours():
    trip = Trip.parse("07:15", "08:45", "17.3")
    trip_time = trip.get_time()
    trip_time.should.equal(90)

def test_get_trip_time_cross_hours_minute_less():
    trip = Trip.parse("07:45", "08:05", "17.3")
    trip_time = trip.get_time()
    trip_time.should.equal(20)

def test_get_trip_speed():
    trip = Trip.parse("07:15", "07:45", "17.3")
    trip_speed = trip.get_speed()
    trip_speed.should.equal(34.6)

def test_get_trip_speed2():
    trip = Trip.parse("06:12", "06:32", "21.8")
    trip_speed = trip.get_speed()
    trip_speed.should.equal(65.4)
