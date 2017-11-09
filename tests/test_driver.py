import sure

from trippy.driver import Driver
from trippy.trip import Trip

def test_add_trip():
    driver = Driver("Dan")
    driver.add_trip(Trip.parse("07:15", "07:45", "17.3"))

    num_trips = len(driver)
    num_trips.should.equal(1)
 
def test_calculate_miles_driven_one_trip():
    driver = Driver("Dan")
    driver.add_trip(Trip.parse("07:15", "07:45", "17.3"))

    miles_driven = driver.get_total_miles_driven()
    miles_driven.should.equal(17.3)

def test_calculate_miles_driven_two_trips():
    driver = Driver("Dan")
    driver.add_trip(Trip.parse("07:15", "07:45", "17.3"))
    driver.add_trip(Trip.parse("06:12", "06:32", "21.8"))

    num_trips = len(driver)
    miles_driven = driver.get_total_miles_driven()

    num_trips.should.equal(2)
    miles_driven.should.equal(39.1)
    
def test_calculate_average_speed_one_trip():
    driver = Driver("Dan")
    driver.add_trip(Trip.parse("07:15", "07:45", "17.3"))

    average_speed = driver.get_average_speed()
    average_speed.should.equal(34.6)

def test_claculate_average_speed_two_trips():
    driver = Driver("Dan")
    driver.add_trip(Trip.parse("07:15", "07:45", "17.3"))
    driver.add_trip(Trip.parse("06:12", "06:32", "21.8"))

    average_speed = driver.get_average_speed()
    average_speed.should.equal(46.92)

def test_claculate_average_speed_no_trips():
    driver = Driver("Dan")

    average_speed = driver.get_average_speed()
    average_speed.should.equal(0)

def xtest_generate_driver_report():
    driver = Driver("Dan")
    driver.add_trip(Trip.parse("07:15", "07:45", "17.3"))
    driver.add_trip(Trip.parse("06:12", "06:32", "21.8"))

    report = driver.get_report()
    report.should.equal("Dan: 39 miles @ 47 mph")

