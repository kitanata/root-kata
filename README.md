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

## Assumptions on Approach

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
use this entire project would be a single file, and probably not tested
(depending on how much I would use the tool, or it's criticality in nature). As
with anything, it all depends. Is this an ETL like thing where I am loading
mission critical data? Am I writing something to quickly analyze some data?  Am
I making a production API? How big is the entire API? Am I writing a patch? Is
this a proof of concept, or a spike of some sort? These are some examples which
would alter my assumptions and thus method of development.

For a simpler implementation, I would use data primitives, named tuples, and
functional programming constructs (like the itertools library). I hope the
folks at Root would appreciate simplicity of design in using data primatives
and functional programming constructs, but I've actually been burned by that
assumption in the past (when it comes to interviews), thus classes.

3. The use of a database isn't needed.

I went back in forth with whether or not I should use something like
sqlalchemy(an ORM) and sqlite3, or if I should simplify with a simple JSON
file to represent a database like structure, or if I should just assume the
files are small enough that the entire program can run in memory on a single
thread/process. Because of the nature of the exercise (and the fact that the
input is basically a flat-file database already), I eliminated the question
altogether.

4. This application use case is more of a utility than something at scale.

It concievable that something like this would need a massive architecture
behind it to service data. I'm sure at Root you are pulling in Terrabytes of
similar data in an hour/day and need to quickly process it. In which case the
question isn't only if you use a database, but how many and what kind of
clusting/sharding scheme you use, how does data pipe through that architecture,
and how do you queue processing of data, parallelize the processing, and other
considerations you might have at scale.

5. The input files are all based in the same timezone.

This is a hard one, because doing anything with dates and times in any language
is actually very difficult to do right. Developers make wayyy to many
assumptions when it comes to times and dates. Since the excercise states that
the times provided never pass over midnight, I am assuming that this tricky
stuff isn't part of your reasoning for making a hire, and that in this data
processor it is safe to assume all the data is in the same timezone. Also, the
times provided aren't ISO8601 so are missing this information anyway. In a
production environment, if I was handed the file and asked to load a database
or do any kind of analytics on it, I would be very suspect of the validity of
the data and it's source.  This goes doubly so for Root, since the ultimate
source is likely a mobile app.

## Testing Approach

The entire codebase was developed using TDD. Red, Green, Refactor and all that.
:)

I've mostly focused on testing the happy path and behavior through the
application. This is generally the approach I take to testing. I feel that
writing tests against a "sad path" before actually seeing the sad path is a
premature optimization and can lead to test bloat. I like to keep tests as
small as possible, and as few as needed.

If you have a larger dataset you are testing this application with, that
dataset could concievably have a line like "driver Dan" vs "Driver Dan". To me
a different casing represents a flaw in the original data, and the
application's failure to handle it (at this point in time), is not a flaw in
the application itself. That to handle different casing for commands (i.e.
equating "Driver" with "driver"), is in fact a feature of the application.

Since that feature was not specified in the requirements, it hasn't been
implemented. Of course, if it needed to be a feature then we would just need to
define it, write a test for it, and implement the test. No biggie.

You will also notice that my tests often have multiple asserts. To me that is
okay. I think the idea that a single test should have a single assert is flawed
because it can restrict the robustness of a test. The point of a test is to
test behavior of a single unit or integration of multiple units. If you need to
use multiple assertions (within reason) to test that behavior/integration, then
that isn't only acceptable but it is desirable.

You'll also notice that I completely setup and tear down each test in it's
entirety. (I don't use test suites or setup and teardown methods.) This is a
preference of mine because it completely decouples the tests from each other
and helps keep them from ossifing the codebase. It also reduces side-effects
between tests. By writing them in this manner, I can be certain that modifying
one test will have no influence on another.

## Retrospective

Overall, I am quite happy with this code. Although I am sure there are ways to
improve it, I feel it is clean, small, and accomplishes the goals and
requirements of the excercise. I went back and forth a few times on using other
idioms in Python. Should I just use dicts and named tuples? Should I use
classes? Should I use itertools, or some fancy library? Should I opt for simple
and straight foward? 

I feel like taking a simple and straight forward approach is the right one in
most cases, so that is what I did here. That has the additional benefit that
non-Python people can understand what you are doing, and it looks rather clean.

Also, you'll notice I didn't use any "design patterns" in my code. I don't do
that, like... ever. If you try to write Python like you write Java, you're
doing it wrong. :)

"Always write your code like the person who must maintain it is a murderous
psycopath who knows where you live." ~ Unknown Dev

