import time
import random
import asyncio

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):

    pivot = array.pop()
    lower = []
    greater = []

    for n in array:
        if pivot <= n:
            greater.append(n)
        else:
            lower.append(n)

    if len(greater) > 1:
        greater = quicksort(greater)

    if len(lower) > 1:
        lower = quicksort(lower)

    return [*lower, pivot, *greater]


# compatible with python 2
def quicksortPython2(array):
    pivot = array.pop()
    lower = []
    greater = []

    for n in array:
        if pivot < n:
            greater.append(n)
        else:
            lower.append(n)

    if len(greater) > 1:
        greater = quicksortPython2(greater)

    if len(lower) > 1:
        lower = quicksortPython2(lower)

    lower.append(pivot)
    lower.extend(greater)

    return lower


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
