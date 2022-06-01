from time import time

def partition(my_list, low, high):
    pivot = my_list[high]
    i = low - 1
    for j in range(low, high):
        if my_list[j] <= pivot:
            i = i + 1
            (my_list[i], my_list[j]) = (my_list[j], my_list[i])
    (my_list[i + 1], my_list[high]) = (my_list[high], my_list[i + 1])
    return i + 1

def quick_sort(my_list, low, high):
    if low < high:
        pi = partition(my_list, low, high)
        quick_sort(my_list, low, pi - 1)
        quick_sort(my_list, pi + 1, high)

def sort(my_list):
    initial = time()
    low = 0
    high = len(my_list) - 1
    quick_sort(my_list, low, high)
    end = time()
    return my_list, float(round(end-initial, 5))