#!/usr/bin/env python
from sys import argv

script, first, second, third = argv

print "The script is called : ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is:", third

print "*" * 20

fullname = raw_input('What is your fullname ?')
age = int(raw_input('How old are you ?'))

print "Your fullname is %s and you're %d age" % (fullname, age)
