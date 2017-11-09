import sure

from trippy.process import Processor

def test_ctor():
    process = Processor()
    (3).should.equal(3)

def test_split_line():
    process = Processor()
    result = process._split_line("Driver Dan")
    result.should.equal(('Driver', 'Dan'))

def test_split_lines_with_times():
    process = Processor()
    result = process._split_line("Trip Dan 07:15 07:45 17.3")
    result.should.equal(('Trip', 'Dan', '07:15', '07:45', '17.3'))

def test_add_driver_has_driver():
    process = Processor()
    process.process_line("Driver Dan")
    result = process.has_driver("Dan")
    result.should.equal(True)

def test_add_driver_get_driver():
    process = Processor()
    process.process_line("Driver Dan")
    result = process.get_driver("Dan")
    str(result).should.equal("Dan")

def test_add_driver_multiple():
    process = Processor()
    process.process_line("Driver Dan")
    process.process_line("Driver Erin")
    process.process_line("Driver Fred")
    dan = process.get_driver("Dan")
    erin = process.get_driver("Erin")
    fred = process.get_driver("Fred")
    str(dan).should.equal("Dan")
    str(erin).should.equal("Erin")
    str(fred).should.equal("Fred")

    num_drivers = len(process)
    num_drivers.should.equal(3)

def test_get_driver_not_found():
    process = Processor()
    result = process.get_driver("Sue")
    result.should.be.none

def test_add_driver_no_dupes():
    process = Processor()
    process.process_line("Driver Dan")
    process.process_line("Driver Dan")

    num_drivers = len(process)
    num_drivers.should.equal(1)

def test_add_trip_for_driver():
    process = Processor()
    process.process_line("Driver Dan")
    process.process_line("Trip Dan 07:15 07:45 17.3")

    dan = process.get_driver("Dan")
    num_trips = len(dan)
    num_trips.should.equal(1)

def test_calculate_miles_driven_for_driver():
    process = Processor()
    process.process_line("Driver Dan")
    process.process_line("Trip Dan 07:15 07:45 17.3")

    dan = process.get_driver("Dan")
    miles_driven = dan.get_miles_driven()
    miles_driven.should.equal(17.3)

# def test_multiple_trips_for_driver():
#     process = Processor()
#     process.process_line("Driver Dan")
#     process.process_line("Trip Dan 07:15 07:45 17.3")
#     process.process_line("Trip Dan 06:12 06:32 21.8")
# 
#     dan = process.get_driver("Dan")
#     num_trips = len(dan)
#     miles_driven = dan.get_miles_driven()
# 
#     num_trips.should.equal(2)
#     miles_driven.should.equal(39.1)
    
