from math import factorial

print("Task 1:")
password = "password123"
if password == "password123":
    print("Password is correct")
else:
    print("Password is incorrect")

print("Task 2:")

days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

day_number_3 = 3
day_number_8 = 8
if day_number_3 in days_of_week:
    print(days_of_week[day_number_3])
else:
    print("Something went wrong")

print("Task 3:")

num = 4
index = 1
while index <= 10:
    print(num * index)
    index += 1

print()

for i in range(1, 11):
    print(f"{i} x {num} = {i * num}")

print("Task 4:")

list_of_numbers = [11, 24, 4, 29, 58, 64]
s = 0

print()

for number in list_of_numbers:
    s += number
print(s)

print(sum(list_of_numbers))

print("Task 5:")

fact = 1
for number in range(1, 6):
    fact *= number

print(fact)

print(factorial(5))

print("Task 6:")

for oven_number in range(1, 51):
    if oven_number % 2 == 0:
        print(oven_number)

print("Task 7:")

a = 1
for simple_number in range(1, 100):
    for n in range(1, simple_number + 1):
        if simple_number % n == 0:
            a *= n
    if a == simple_number:
        print(simple_number)
    a = 1
