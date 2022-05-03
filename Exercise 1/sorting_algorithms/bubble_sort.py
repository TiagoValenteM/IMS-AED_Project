from time import time

def sort(my_list):
    initial = time()
    for list_index in range(0, len(my_list)):
        for element_index in range(0, len(my_list) - 1):
            if my_list[element_index] > my_list[element_index + 1]:
                swapping_two_elements(my_list, element_index, element_index + 1)
    end = time()
    return my_list, float(round(end-initial, 5))

def swapping_two_elements(list_to_sort, position_1, position_2):
    temp = list_to_sort[position_1]
    list_to_sort[position_1] = list_to_sort[position_2]
    list_to_sort[position_2] = temp