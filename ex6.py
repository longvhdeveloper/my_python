#!/usr/bin/env python
#khai bao chuoi va dung noi suy la mot so
x = "There are %d types of people." % 10
#khai bao bien
binary = "binary"
#khai bao bien
do_not = "don't"
#khai bao chuoi va dung phuong thuc noi suy bien la kieu chuoi
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
print "I said %r." % x
print "I also said '%s'" % y

#khai bao bien la kieu boolean
hilarious = False
#khai bao bien co kieu noi suy la mot kieu du do
#%r thuong dung de debug, in gia tri cua bien duoc truyen vao
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation

print joke_evaluation % hilarious

#khai bao mot chuoi
w = "This is the left side of..."
#khai bao mot chuoi
e = "a string with a right side"
#in ghep 2 chuoi lai
print w + e