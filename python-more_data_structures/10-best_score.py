#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) is 0:
        return None
    bigValue = max(a_dictionary, key=lambda x: a_dictionary[x])
    return bigValue
