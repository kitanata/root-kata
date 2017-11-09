import os
import sys
import sure

import subprocess as sp

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

    report_string = '\n'.join(process.get_report())
    (''.join(lines)).should.equal(report_string + '\n')

def test_app_interface():
    app_path = os.path.join(os.getcwd(), 'app.py')
    file_path = os.path.join(os.getcwd(), 'tests/fixtures/big_test_file.txt')

    proc = sp.Popen([sys.executable, app_path, file_path], 
                    cwd=os.getcwd(), 
                    env=os.environ.copy(),
                    stdout=sp.PIPE, 
                    stderr=sp.PIPE)
    stdout, _ = proc.communicate()

    stdout = stdout.decode('utf8')

    lines = []
    with open(fixture_path('big_test_report.txt'), 'r') as f:
        lines = f.readlines()

    (''.join(lines)).should.equal(stdout)
