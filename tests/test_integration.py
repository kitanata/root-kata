import os
import sure

from trippy.process import Processor

def fixture_path(path):
    return os.path.join(os.getcwd(), 'tests/fixtures', path)

def test_big_file():
    process = Processor()

    with open(fixture_path('big_test_file.txt'), 'r') as f:
        while True:
            line = f.readline()

            if not line:
                break;

            process.process_line(line)

    lines = []
    with open(fixture_path('big_test_report.txt'), 'r') as f:
        lines = f.readlines()

    (''.join(lines)).should.equal(process.report())
