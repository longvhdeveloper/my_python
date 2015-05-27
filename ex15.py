#import module
from sys import argv

#asign variable from command line
script, filename = argv

#open file
txt = open(filename)

#print content
print "Here's your filename %r: " % filename

#get file conent
print txt.read()

#close file
txt.close()

#get file name from input command line
filename_again = raw_input('Type the filename again: ')

#open file
txt_again = open(filename_again)

#print file content
print txt_again.read()

#close file
txt_again.close
