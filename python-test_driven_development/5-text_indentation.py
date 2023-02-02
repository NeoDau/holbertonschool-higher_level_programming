#!/usr/bin/python3
"""shebang"""


def text_indentation(text):
    """Print Characters - "." "?" ":" """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for x in range(len(text)):
        if text[x] == "." or text[x] == "?" or text[x] == ":":
            print(text[x] + "\n")
        if x + 1 == " ":
            continue
        else:
            print(text[x], end="")
