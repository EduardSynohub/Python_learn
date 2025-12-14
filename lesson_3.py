from math import factorial

password = "password123"
if password == "password123":
    print("Password is correct")
else:
    print("Password is incorrect")

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

num = 4
index = 1
while index <= 10:
    print(num * index)
    index += 1

for i in range(1, 11):
    print(f"{i} x {num} = {i * num}")

list_of_numbers = [11, 24, 4, 29, 58, 64]
s = 0

for number in list_of_numbers:
    s += number

print(s)

print(sum(list_of_numbers))

f = 1
for number in range(1, 6):
    f *= number

print()

for oven_numbers in range(1, 51):
    if oven_numbers % 2 == 0:
        print(oven_numbers)