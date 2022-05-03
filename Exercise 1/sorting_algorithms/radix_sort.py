from time import time

def counting_sort(my_list, digit1):
    len_list = len(my_list)
    output = [0] * (len_list)
    count = [0] * (10)
    for i in range(0, len_list):
        index = my_list[i] // digit1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len_list - 1
    while i >= 0:
        index = my_list[i] // digit1
        output[count[index % 10] - 1] = my_list[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, len(my_list)):
        my_list[i] = output[i]

def sort(my_list):
    initial = time()
    max1 = max(my_list)
    digit = 1
    # digit is an indicator for the number position we are comparing, example: digit = 1 == 1; digit = 3 == 100
    while max1 / digit > 0:
        counting_sort(my_list, digit)
        digit *= 10
    end = time()
    return my_list, float(round(end-initial, 5))

