from time import time

def sort(my_list):
    if len(my_list) <= 1:
        return my_list
    middle = len(my_list)//2
    left = sort(my_list[:middle])
    right = sort(my_list[middle:])
    return merge(left, right)

def merge(left_list, right_list):
    my_list = []
    i = j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            my_list.append(left_list[i])
            i += 1
        else:
            my_list.append(right_list[j])
            j += 1
    my_list.extend(left_list[i:])
    my_list.extend(right_list[j:])
    return my_list