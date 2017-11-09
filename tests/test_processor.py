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

def test_process_two_trips_for_one_driver():
    process = Processor()
    process.process_line("Driver Dan")
    process.process_line("Trip Dan 07:15 07:45 17.3")
    process.process_line("Trip Dan 06:12 06:32 21.8")

    dan = process.get_driver("Dan")
    num_trips = len(dan)
    miles_driven = dan.get_total_miles_driven()
    average_speed = dan.get_average_speed()

    num_trips.should.equal(2)
    miles_driven.should.equal(39.1)
    average_speed.should.equal(46.92)

def test_discard_trips_for_undefined_drivers():
    process = Processor()
    process.process_line("Trip Dan 07:15 07:45 17.3")
    process.process_line("Driver Dan")
    process.process_line("Trip Dan 06:12 06:32 21.8")

    dan = process.get_driver("Dan")
    num_trips = len(dan)
    miles_driven = dan.get_total_miles_driven()
    average_speed = dan.get_average_speed()

    num_trips.should.equal(1)
    miles_driven.should.equal(21.8)
    average_speed.should.equal(65.4)


def test_discard_trips_faster_than_100mph():
    process = Processor()
    process.process_line("Driver Dan")
    process.process_line("Trip Dan 06:45 07:45 100.1")
    process.process_line("Trip Dan 06:12 06:32 21.8")

    dan = process.get_driver("Dan")
    num_trips = len(dan)
    miles_driven = dan.get_total_miles_driven()
    average_speed = dan.get_average_speed()

    num_trips.should.equal(1)
    miles_driven.should.equal(21.8)
    average_speed.should.equal(65.4)

def test_discard_trips_slower_than_5mph():
    process = Processor()
    process.process_line("Driver Dan")
    process.process_line("Trip Dan 06:45 07:45 4.9")
    process.process_line("Trip Dan 06:12 06:32 21.8")

    dan = process.get_driver("Dan")
    num_trips = len(dan)
    miles_driven = dan.get_total_miles_driven()
    average_speed = dan.get_average_speed()

    num_trips.should.equal(1)
    miles_driven.should.equal(21.8)
    average_speed.should.equal(65.4)

def test_process_report_generation():
    process = Processor()
    process.process_line("Driver Dan")
    process.process_line("Driver Alex")
    process.process_line("Driver Bob")
    process.process_line("Trip Dan 07:15 07:45 17.3")
    process.process_line("Trip Dan 06:12 06:32 21.8")
    process.process_line("Trip Alex 12:01 13:16 42.0")

    report = process.get_report()
    report[0].should.equal("Alex: 42 miles @ 34 mph")
    report[1].should.equal("Dan: 39 miles @ 47 mph")
    report[2].should.equal("Bob: 0 miles")

