import sure

from trippy.process import Processor

def test_ctor():
    process = Processor()
    (3).should.equal(3)
