from time import time

def sort(my_list):
    initial = time()
    for index in range(len(my_list)):
        min_index = index
        for index_element in range(index+1, len(my_list)):
            if my_list[index_element] < my_list[min_index]:
                min_index = index_element
        swapping(my_list, min_index, index)
    end = time()
    return my_list, float(round(end-initial, 5))


def swapping(list_to_sort, position_1, position_2):
    temp = list_to_sort[position_1]
    list_to_sort[position_1] = list_to_sort[position_2]
    list_to_sort[position_2] = temp
