# Bloom Sets

This is very much a work-in-progress.  Normally, I don't publish anything in
this raw a state, but I haven't touched this in a few weeks, and don't want to
lose it.

I'm trying to come up with an efficient implementation of a bloom set in
python, and answer a few questions along the way.

For example, how many elements can a bloom set hold (in proportion to its size)
before it becomes useless (due to collisions)?

Under what conditions are bloom sets useful?  When do they outperform built-in
`set`s?


Currently, one of my implementation beats out the built-in `set`s in some
cases, but only using pypy. This raises more questions.


In short, there's still a lot I need to figure out before calling this "done".
