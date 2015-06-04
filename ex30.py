#!/usr/bin/env python
people = 10
cars = 15
trucks = 20

if cars > people:
    print "We should take care cars."
elif cars < people:
    print "We should not take care the cars"
else:
    print "We can't decide."

if trucks > cars and people < trucks:
    print "That's too many trucks"
elif trucks < cars or people > trucks:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide"

if people > trucks:
    print "Alright, let's just take the trucks"
else:
    print "Fine, let's stay home then."
