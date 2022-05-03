from time import time

# n is size of heap
def heap(my_list, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and my_list[i] < my_list[left]:
        largest = left
    if right < n and my_list[largest] < my_list[right]:
        largest = right
    if largest != i:
        my_list[i], my_list[largest] = my_list[largest], my_list[i]  # swap
        # Heap the root
        heap(my_list, n, largest)

def sort(my_list):
    initial = time()
    n = len(my_list)
    for i in range(n // 2 - 1, -1, -1):
        heap(my_list, n, i)
    for i in range(n - 1, 0, -1):
        my_list[i], my_list[0] = my_list[0], my_list[i]  # swap
        heap(my_list, i, 0)
    end = time()
    return my_list, float(round(end-initial, 5))
