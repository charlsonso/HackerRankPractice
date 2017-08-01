#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    l = []
    for i in grades:
        if i<38:
            l.append(i)
        elif i%5>2:
            j = i+5-(i%5)
            l.append(j)
        else:
            l.append(i)
    return l

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


