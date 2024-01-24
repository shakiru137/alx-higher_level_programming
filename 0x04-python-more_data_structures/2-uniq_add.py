#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_sum = 0
    unique_list = list(set(my_list))
    for i in range(len(unique_list)):
        list_sum += unique_list[i]
    return list_sum
