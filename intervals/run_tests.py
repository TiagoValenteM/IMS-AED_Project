from functions import new_interval, matrix_increase, sort_matrix, final_list

# asking for an input from the user
user_interval = []
new_interval(user_interval)

# append it on a matrix
unorganized_matrix = []
unorganized_matrix.append(user_interval)

# print the first input
print(final_list(unorganized_matrix))

while True:
    print()
    question = input("Do you want to add another interval? Please answer with << yes >> or << no >> ")
    if question.lower() == "yes":
        user_interval = []
        new_interval(user_interval)
        matrix_increase(user_interval, unorganized_matrix)
        sort_matrix(unorganized_matrix)
        print()
        print(final_list(unorganized_matrix))
    elif question.lower() == "no":
        print()
        print(final_list(unorganized_matrix))
        break
