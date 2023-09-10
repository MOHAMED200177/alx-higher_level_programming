#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not (idx < 0 or idx > len(my_list) - 1):
        newList = my_list[:]
        newList[idx] = element
        return newList
    return my_list
