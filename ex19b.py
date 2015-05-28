#!/usr/bin/env python
from sys import argv

script, number1, number2 = argv

number1 = int(number1)
number2 = int(number2)


def add_two_number(number1, number2):
    print "%d + %d = %d" % (number1, number2, number1 + number2)

add_two_number(number1, number2)
add_two_number(1, 2)

number1 = 10
number2 = 15
add_two_number(number1, number2)

number1 = int(raw_input('Number 1 : '))
number2 = int(raw_input('Number 2 : '))

add_two_number(number1, number2)

add_two_number(10 + 20, 50 + 18)

add_two_number(number1 + 8, number2 + 12)
