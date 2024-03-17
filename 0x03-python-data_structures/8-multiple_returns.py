#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        length = len(sentence)
        first_char = None
        if length > 0:
            first_char = sentence[0]
        return (length, first_char)
    return(None)
