#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 0, None
    else:
        my_list.sort()
        return (my_list[-1])
