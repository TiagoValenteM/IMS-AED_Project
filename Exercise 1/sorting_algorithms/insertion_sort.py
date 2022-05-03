from time import time

def sort(my_list):
    initial = time()
    for index in range(1, len(my_list)):
        current = my_list[index]
        position = index
        while position > 0 and current < my_list[position - 1]:
            my_list[position] = my_list[position - 1]
            position = position - 1
        my_list[position] = current
    end = time()
    return my_list, float(round(end-initial, 5))