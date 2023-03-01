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

first_row_input_char_values = []

for letter in first_row_input:
    value = ord(letter)

    first_row_input_char_values.append(value)

first_row_input_char_sum = sum(first_row_input_char_values)

first_row_solution_char_values = []

for letter in first_row_solution:
    value = ord(letter)

    first_row_solution_char_values.append(value)

first_row_solution_char_sum = sum(first_row_solution_char_values)

#########################################################################################

second_row_input_char_values = []

for letter in second_row_input:
    value = ord(letter)

    second_row_input_char_values.append(value)

second_row_input_char_sum = sum(second_row_input_char_values)

second_row_solution_char_values = []

for letter in second_row_solution:
    value = ord(letter)

    second_row_solution_char_values.append(value)

second_row_solution_char_sum = sum(second_row_solution_char_values)

#########################################################################################

third_row_input_char_values = []

for letter in third_row_input:
    value = ord(letter)

    third_row_input_char_values.append(value)

third_row_input_char_sum = sum(third_row_input_char_values)

third_row_solution_char_values = []

for letter in third_row_solution:
    value = ord(letter)

    third_row_solution_char_values.append(value)

third_row_solution_char_sum = sum(third_row_solution_char_values)

#########################################################################################

rounds = []
rounds_counter = 0

first_row_flag = first_row_input_char_sum == first_row_solution_char_sum
second_row_flag = second_row_input_char_sum == second_row_solution_char_sum
third_row_flag = third_row_input_char_sum == third_row_solution_char_sum

if first_row_flag and second_row_flag and third_row_flag:
    first_row_check()
    second_row_check()
    third_row_check()

    print(rounds)
    
    for _ in range(len(rounds)):
        rounds_counter += 1

    print(rounds_counter)

else:
    print('Impossível')
