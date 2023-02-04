#!/usr/bin/python3
"""shebang"""


def text_indentation(text):
    """Print Characters - "." "?" ":" """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    characters = 0
    for char in range(len(text)):
        if text[char] == "." or text[char] == "?" or text[char] == ":":
            print(text[char] + "\n")
            characters = 1
        if characters == 1:
            if text[char + 1] == " ":
                continue
            characters = 0
        else:
            print(text[char], end="")
