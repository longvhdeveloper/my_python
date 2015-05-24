#!/usr/bin/env python
from sys import argv

script, username, email = argv
prompt = "> "

print "Hi %s, I'm %s script." % (username, script)
print "I'd like to ask you a few question."
print "Do you like me %s ?" % username
likes = raw_input(prompt)

print "Where do you live %s ?" % username
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
And I will send to your email %r
Have good day
""" % (likes, lives, computer, email)
