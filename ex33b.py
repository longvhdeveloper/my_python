#!/usr/bin/env python
def loop_data(x):
    elements = []
    if x <= 0:
        return elements
    else:
        i = 0
        while i < x:
            elements.append(i)
            i += 1
    return elements


for i in range(0, 6):
    print i
