from sys import argv

script, filename = argv

file_object = open(filename)
print "Content of file %r :" % filename
print file_object.read()
file_object.close()
