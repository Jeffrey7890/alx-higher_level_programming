#!/usr/bin/python3

def text_indentation(text):
    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in ['.', ';', '?', '']:
            if text[i + 1] == ' ':
                i += 1
            print('\n')
        i += 1
