print("Task 1:")
list_of_numbers = [11, 18, 23, 4, 56, 24, 48]
list_of_numbers.append(10)
list_of_numbers.append(20)
list_of_numbers.remove(10)
print(list_of_numbers)

print("Task 2:")

sum_of_numbers = sum(list_of_numbers)
print(sum_of_numbers)

print("Task 3:")

list_of_double_numbers = []
for number in list_of_numbers:
    list_of_double_numbers.append(number * 2)

print(list_of_double_numbers)