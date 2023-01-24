#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        return (0, "none")
    else:
        b = sentence[0]

    return (a, b)
