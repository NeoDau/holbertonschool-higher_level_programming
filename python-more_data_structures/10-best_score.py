#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    bigValue = max(a_dictionary, key=lambda x: a_dictionary[x])
    return bigValue
