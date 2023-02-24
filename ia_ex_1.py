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

i = 0

for letter in first_row_input:
    if letter == first_row_solution[i]:
        print('y')
        i += 1
    else:
        temp_index_0 = first_row_input[0]
        temp_index_1 = first_row_input[1]
        temp_index_2 = first_row_input[2]

        first_row_input[0] = temp_index_1
        first_row_input[1] = temp_index_2
        first_row_input[2] = temp_index_0

        print(first_row_input, '\trodou')
        i += 1
