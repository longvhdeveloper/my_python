#!/usr/bin/env python
#create variable formatter have formatter
formatter = "%r %r %r %r"

#print formatter with formtter is number
print formatter % (1, 2, 3, 4)
#print formatter with formatter is string
print formatter % ('one', 'two', 'three', 'four')
#print formatter with formatter is formatter variable
print formatter % (formatter, formatter, formatter, formatter)
#print formatter with formatter is string
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing",
    "So I said goodnight"
)