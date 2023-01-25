#!/usr/bin/pyython3
def common_elements(set_1, set_2):
    newElement = []
    for x in set_1:
        if x in set_2:
            newElement.append(x)
    return(newElement)
