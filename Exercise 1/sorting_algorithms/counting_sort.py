from time import time

def sort(my_list):
    initial = time()
    max_element = int(max(my_list))
    min_element = int(min(my_list))
    range_of_elements = max_element - min_element + 1
    count_list = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(my_list))]

    for i in range(0, len(my_list)):
        count_list[my_list[i] - min_element] += 1
    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]
    for i in range(len(my_list) - 1, -1, -1):
        output_arr[count_list[my_list[i] - min_element] - 1] = my_list[i]
        count_list[my_list[i] - min_element] -= 1
    for i in range(0, len(my_list)):
        my_list[i] = output_arr[i]
    end = time()
    return my_list, float(round(end-initial, 5))