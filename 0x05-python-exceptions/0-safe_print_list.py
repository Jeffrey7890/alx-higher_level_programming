#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for i in range(x):
            print(my_list[i], end="")
            n += 1
    except Exception:
        pass
    print("")
    return (n)
