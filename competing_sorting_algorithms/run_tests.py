from sorting_algorithms import bubble_sort, counting_sort, heap_sort, insertion_sort, merge_sort, quick_sort, \
    radix_sort, \
    selection_sort
from user_inputs import user_input
from random import randint


def time(time_sec):
    return f'{time_sec:.5f} sec'


# initial list input
ini_input = input("What is the initial size of your list? ")
initial = user_input(ini_input)

# incremental list input
inc_input = input("What is the incremental size of your list? ")
incremental = user_input(inc_input)

# number of iterations
iti_input = int(input("How many iterations do you want on your list? "))

# range of random numbers
range_input = input("What is the range of random numbers in your list? ")
range_numbers = user_input(range_input)


iterations_result = []
algorithms_result = []
bubble_result = []
counting_result = []
heap_result = []
insertion_result = []
merge_result = []
quick_result = []
radix_result = []
selection_result = []

for number in range(iti_input):
    iterations_result.append(number + 1)
    values_list = [randint(0, range_numbers) for i in range(initial + incremental * number)]
    algorithms_result.append(initial + incremental * number)
    bubble_sorted, bubble_time = bubble_sort.sort(values_list.copy())
    bubble_result.append(time(bubble_time))
    counting_sorted, counting_time = counting_sort.sort(values_list.copy())
    counting_result.append(time(counting_time))
    heap_sorted, heap_time = heap_sort.sort(values_list.copy())
    heap_result.append(time(heap_time))
    insertion_sorted, insertion_time = insertion_sort.sort(values_list.copy())
    insertion_result.append(time(insertion_time))
    merge_sorted, merge_time = merge_sort.sort(values_list.copy())
    merge_result.append(time(merge_time))
    quick_sorted, quick_time = quick_sort.sort(values_list.copy())
    quick_result.append(time(quick_time))
    radix_sorted, radix_time = radix_sort.sort(values_list.copy())
    radix_result.append(time(radix_time))
    selection_sorted, selection_time = selection_sort.sort(values_list.copy())
    selection_result.append(time(selection_time))

matrix = [["Iteration", iterations_result],
          ["Algorithm", algorithms_result],
          ["Bubble Sort", bubble_result],
          ["Counting Sort", counting_result],
          ["Heap Sort", heap_result],
          ["Insertion Sort", insertion_result],
          ["Merge Sort", merge_result],
          ["Quick Sort", quick_result],
          ["Radix Sort", radix_result],
          ["Selection Sort", selection_result]]

dash = '-' * ((iti_input+1) * 26)
for line in matrix:
    print(f'\n{dash}')
    print(f'{line[0]:<20s}', end='')
    for secs in line[1]:
        sep = '|'
        print(f"{sep:3s}", end='')
        print(f'{str(secs):<25s}', end='')
print()
print()

