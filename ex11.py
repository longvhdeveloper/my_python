#!/usr/bin/env python
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age,
                                                    height,
                                                    weight)

print "*" * 20
print "What's your fullname ?",
fullname = str(raw_input())
print "How many people in your family ?",
number_people = int(raw_input())
print "How many point you have in last match ?",
point = float(raw_input())

print "So, Your fullname is %s\nYour family have %d member \nAnd you have %.2f point in last match" % (fullname, number_people, point)
