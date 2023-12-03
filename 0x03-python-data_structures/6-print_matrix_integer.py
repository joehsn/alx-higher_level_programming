#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        lvar = 1
        for j in i:
            if lvar == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            lvar = lvar + 1
        print()
