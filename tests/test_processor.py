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

