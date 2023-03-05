def first_row_check():
    i = 0

    for letter in first_row_input:
        if letter == first_row_solution[i]:
            i += 1

        else:
            temp_index_0 = first_row_input[0]
            temp_index_1 = first_row_input[1]
            temp_index_2 = first_row_input[2]

            first_row_input[0] = temp_index_2
            first_row_input[1] = temp_index_0
            first_row_input[2] = temp_index_1

            print(first_row_input)

            rounds.append('R1')

            i += 1

    print()


def second_row_check():
    i = 0

    for letter in second_row_input:
        if letter == second_row_solution[i]:
            i += 1

        else:
            temp_index_0 = second_row_input[0]
            temp_index_1 = second_row_input[1]
            temp_index_2 = second_row_input[2]

            second_row_input[0] = temp_index_2
            second_row_input[1] = temp_index_0
            second_row_input[2] = temp_index_1

            print(second_row_input)

            rounds.append('R2')

            i += 1

    print()


def third_row_check():
    i = 0

    for letter in third_row_input:
        if letter == third_row_solution[i]:
            i += 1

        else:
            temp_index_0 = third_row_input[0]
            temp_index_1 = third_row_input[1]
            temp_index_2 = third_row_input[2]

            third_row_input[0] = temp_index_2
            third_row_input[1] = temp_index_0
            third_row_input[2] = temp_index_1

            print(third_row_input)

            rounds.append('R3')

            i += 1

    print()


#########################################################################################

first_row_input = input("First row input: ").split()
second_row_input = input("Second row input: ").split()
third_row_input = input("Third row input: ").split()

first_row_solution = input("First row solution: ").split()
second_row_solution = input("Second row solution: ").split()
third_row_solution = input("Third row solution: ").split()

print()

print("User input: ")
print(first_row_input)
print(second_row_input)
print(third_row_input)

print()

print("Expected solution: ")
print(first_row_solution)
print(second_row_solution)
print(third_row_solution)

print()

#########################################################################################

rounds = []
rounds_counter = 0

first_row_index_check = first_row_input[0] in first_row_solution and first_row_input[1] in first_row_solution and first_row_input[2] in first_row_solution
second_row_index_check = second_row_input[0] in second_row_solution and second_row_input[1] in second_row_solution and second_row_input[2] in second_row_solution
third_row_index_check = third_row_input[0] in third_row_solution and third_row_input[1] in third_row_solution and third_row_input[2] in third_row_solution

if first_row_index_check and second_row_index_check and third_row_index_check:
    first_row_check()
    second_row_check()
    third_row_check()

    print(rounds)
    
    for _ in range(len(rounds)):
        rounds_counter += 1

    print(rounds_counter)

else:
    print('Impossível')
