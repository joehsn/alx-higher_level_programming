#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    for num in range(0, len(my_list)):
        if num == idx:
            return my_list[num]
