# _*_ coding:utf-8 _*_
my_name = "Jackie Wu"
my_age = 26 #real age
my_height = 170 #cm
my_height_in_inch = my_height / 2.5
my_weight = 80 #kgs
my_weight_in_pounds = my_weight * 2.02
my_eyes = "Black"
my_teeth = "White"
my_hair = "Black"

print "Let's talk about %s ." % my_name
print "He's %d cm tall." % my_height,
print "He's %.2f inch tall" % my_height_in_inch
print "He's %d kg heavy" % my_weight
print "He's %.2f pounds heavy" % my_weight_in_pounds
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

#this is other way
print "If I add %s, %d and %d I get %d." % (my_name, my_height, my_weight, my_age + my_weight + my_height)

print "If I add %r, %d and %d I get %d." % (my_name, my_height, my_weight, my_age + my_weight + my_height)
