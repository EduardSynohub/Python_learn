from methods import calculator as calc
from methods import utilities as utils

print("Task 1")

num_1 = 10
num_2 = 5
num_3 = 0

print(calc.add(num_1, num_2))
print(calc.subtract(num_1, num_2))
print(calc.multiply(num_1, num_2))
print(calc.divide(num_1, num_2))

print("Task 2")

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(utils.calculate_average(list_of_numbers))
print(utils.find_max(list_of_numbers))