#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(())
    for item in my_list:
        my_set.add(item)
    return len(my_set)
