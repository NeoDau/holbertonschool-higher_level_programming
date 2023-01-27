#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDictionary = a_dictionary.copy()
    for x in newDictionary:
        newDictionary[x] *= 2
    return newDictionary
