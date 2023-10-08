#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list_mul = []

    for i in my_list:
        if i % 2 == 0:
            new_list_mul.append(True)
        else:
            new_list_mul.append(False)

    return (new_list_mul)
