from sorting_algorithms import bubble_sort, counting_sort, heap_sort, insertion_sort, quick_sort, radix_sort, \
    selection_sort
from user_inputs import list_initial, list_iti, iteration_add


def print_time(time_sec):
    return (f'To sort it took: {time_sec:.5f} seconds.')


# initial list input
ini_input = input("What is the initial size of your list? ")
initial = list_initial(ini_input)
print(initial)

# incremental list input
inc_input = input("What is the incremental size of your list? ")
incremental = list_initial(inc_input)
print(incremental)

# number of iterations
iti_input = input("How many iterations do you want on your list? ")
iteration = list_iti(iti_input)
print(iti_input)

# program adds incremental size times iteration to the initial size
#competing = iteration_add(initial, incremental, iteration)
#print(competing)

#iteracoes = 7
#initial_size = 100
#k
#incr_size = 50
#k
#for i in range(0, iteracoes) {
#list_size = initial_size + incr_size * i
## isto calcula o tamanho da lista, se i = 0, então tens a lista inicial
#list = init_list(list_size)
#results = run_sorts()

bubble_sorted, bubble_time = bubble_sort.sort(initial.copy())
counting_sorted, counting_time = counting_sort.sort(initial.copy())
heap_sorted, heap_time = heap_sort.sort(initial.copy())
insertion_sorted, insertion_time = insertion_sort.sort(initial.copy())
# merge_sorted, merge_time = merge_sort.sort(initial.copy())
quick_sorted, quick_time = quick_sort.sort(initial.copy())
radix_sorted, radix_time = radix_sort.sort(initial.copy())
selection_sorted, selection_time = selection_sort.sort(initial.copy())

print(bubble_sorted)
print("Bubble Sort. " + str(print_time(bubble_time)))
print(counting_sorted)
print("Counting Sort. " + str(print_time(counting_time)))
print(heap_sorted)
print("Heap Sort. " + str(print_time(heap_time)))
print(insertion_sorted)
print("Insertion Sort. " + str(print_time(insertion_time)))
# print (merge_sorted)
# print("Merge Sort. " + str(print_time(merge_time)))
print(quick_sorted)
print("Quick Sort. " + str(print_time(quick_time)))
print(radix_sorted)
print("Radix Sort. " + str(print_time(radix_time)))
print(selection_sorted)
print("Selection Sort. " + str(print_time(selection_time)))
