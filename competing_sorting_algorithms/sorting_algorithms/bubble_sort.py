from time import time

def sort(my_list):
    initial = time()
    list_sorted = sort_recursive(my_list)
    end = time()
    return list_sorted, float(round(end - initial, 5))

def sort_recursive(my_list):
    for list_index in range(0, len(my_list)):
        for element_index in range(0, len(my_list) - 1):
            if my_list[element_index] > my_list[element_index + 1]:
                swapping_two_elements(my_list, element_index, element_index + 1)
    return my_list

def swapping_two_elements(list_to_sort, position_1, position_2):
    temp = list_to_sort[position_1]
    list_to_sort[position_1] = list_to_sort[position_2]
    list_to_sort[position_2] = temp
