#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit))
    return last_digit
