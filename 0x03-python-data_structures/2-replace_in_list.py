#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    for num in range(0, len(my_list)):
        if num == idx:
            my_list[num] = element
            return my_list