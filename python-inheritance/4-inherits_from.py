#!/usr/bin/python3
"""shebang"""


def inherits_from(obj, a_class):
    """Initializanding function"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
