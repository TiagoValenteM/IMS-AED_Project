from random import randint


def new_interval(user_interval):
    lower = int(input("Please, enter the lowest value of the interval: "))
    if lower < -999:
        print("Invalid number. Please enter another one.")
        lower = int(input("Please, enter the lowest value of the interval: "))
    higher = int(input("Please, enter the highest value of the interval: "))
    if higher > 999:
        print("Invalid number. Please enter another one.")
        higher = int(input("Please, enter the highest value of the interval: "))

    for i in range(lower, higher + 1):
        user_interval.append(i)
    return user_interval, lower, higher


def is_pair(number):
    return number % 2 == 0


def shuffle_list(list):
    for i in range(len(list) - 1, 0, -1):
        # Pick a random index from 0 to i
        j = randint(0, i)
        # Swap list[i] with the element at random index
        list[i], list[j] = list[j], list[i]


def counting_sort(my_list):
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
    return my_list


def sort_matrix(matrix):
    for index, interval in enumerate(matrix):
        if is_pair(index + 1):
            shuffle_list(interval)
        else:
            counting_sort(interval)


def get_extremes(interval):
    minimum = interval[0]
    maximum = interval[0]
    for number in interval:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum


def remove_common(interval, user_interval, matrix):
    for number in interval[:]:
        if number in user_interval:
            interval.remove(number)
            user_interval.remove(number)
    if len(interval) == 0:
        matrix.remove(interval)
    return user_interval


def matrix_increase(user_interval, unorganized_matrix):
    index_to_insert = None
    for index, interval in enumerate(unorganized_matrix):
        min, max = get_extremes(interval)
        # continuous case
        if user_interval[0] == max + 1 or user_interval[-1] == min - 1:
            for element in user_interval:
                interval.append(element)
            index_to_insert = None
            break
        # noncontinuous case
        # user_interval that comes after
        if user_interval[0] > max:
            if user_interval[-1] - max >= 2:
                index_to_insert = index + 1
        # user_interval that comes before
        elif user_interval[-1] < min:
            if max - user_interval[-1] >= 2:
                unorganized_matrix.insert(index, user_interval)
                index_to_insert = None
                break
        else:  # overlapping case
            remove_common(interval, user_interval, unorganized_matrix)
            if len(user_interval) > 0:
                matrix_increase(user_interval, unorganized_matrix)
                index_to_insert = None
            break
    if index_to_insert is not None:
        unorganized_matrix.insert(index_to_insert, user_interval)


def final_list(matrix):
    final_print = []
    for i in matrix:
        for j in i:
            final_print.append(j)
    return final_print
