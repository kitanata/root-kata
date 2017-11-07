# Root Coding Challenge

## Project Dependencies

- Python3.5+
- virtualenv
- pip

## Project Setup

1. Create a new virtual environment, and install the python dependencies.

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

2. Run the tests.

```bash
pytest
```

## Architecture Reasoning

Assumptions.

1. The input filesize is smallish. Say less than 1GB in size.

I made the first assumption primarily to justify the lack of complexity in
writing something larger to parallelize work, or to split up the files. I am
assuming that the entire program can run in memory. The flat format provided
does lend itself to something that might be parallelized but the nature of the
assignment makes me believe this isn't something I need to think about for the
purposes of this excercise.

2. The feature set is a starting point for a larger project.

I made the second assumption primarily to justify the over-engineering done
here in order to communicate how I would approach a larger, or longer lasting
project. If I was merely writing a tool to parse and process data for my own
use this entire project would be a single, and probably not tested (depending
on how much I would use the tool, or it's criticality in nature). As with
anything, it all depends. Is this an ETL like thing where I am loading mission
critical data? Am I writing something to quickly analyze some data?  Am I
making a production API? How big is the entire API? Am I writing a patch? Is
this a proof of concept, or a spike of some sort? These are some examples which
would alter my assumptions and thus method of development.

For a simpler implementation, I would use data primitives, named tuples, and
functional programming constructs (like the itertools library). I opted for
classes, because its a bit lowest common denominator for interview questions. I
would hope that Root would appreciate simplicity of design in using data
primatives and functional programming constructs, but I've actually been burned
by that assumption in the past (when it comes to interviews), thus classes.

3. The use of a database isn't needed.

I went back in forth with whether or not I should use something like
sqlalchemy(an ORM) and sqlite3, or if I should simplify with a simple JSON
file to represent a database like structure, or if I should just assume the
files are small enough that the entire program can run in memory on a single
thread/process. Because of the nature of the exercise (and the fact that the
input is basically a flat-file database already), I eliminated the question
altogether.

3. The input files are all based in the same timezone.

This is a hard one, because doing anything with dates and times in any language
is actually very difficult to do right. People make wayyy to many assumptions
when it comes to times and dates. Since the excercise states that the times
provided never pass over midnight, I am assuming that this tricky stuff isn't
part of your reasoning for making a hire, and that this data processor is safe
to assume all the data is in the same timezone. Also, the times provided aren't
ISO8601 so are missing this information anyway. In a production environment, if
I was handed the file and asked to load a database or do any kind of analytics
on it, I would be very suspect of the validity of the data and it's source.
This goes doubly so for Root, since the ultimate source is likely a mobile app.
