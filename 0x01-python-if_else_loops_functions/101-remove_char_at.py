#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    length = len(str)
    if (n > length or n < 0):
        return(str)
    for i in range(len(str)):
        if (str[i] != str[n]):
            cpy += str[i]
    return (cpy)


print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
