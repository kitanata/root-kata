import sure

def inc(x):
    return x + 1

def test_answer():
    (3).should.equal(inc(2))
