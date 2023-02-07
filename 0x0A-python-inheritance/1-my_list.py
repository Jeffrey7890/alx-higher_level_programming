#!/usr/bin/python3
"""prints sorted list men"""


class MyList(list):
    """class inherites from
        the list class
    """
    def print_sorted(self):
        """prints the sorted
            version of itself
        """
        print(sorted(self))
