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

print("Task 4:")

fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

print("Task 5:")

tuple_1 = (1, 4, 23, 11, 43)
tuple_2 = (4, 43, 22, 18)

tuple_3 = tuple_1 + tuple_2
print(tuple_3)

print("Task 6:")

sport_mans = {"name": "Michael", "surname": "Jordan", "age": 25, "team": "Chickago Bulls"}
print(sport_mans)

print("Task 7:")

books = {"author": "Rowling", "year": 2000}
print(books)
book_update = {"author": "Jack", "year": 1994}
books.update(book_update)
print(books)

print("Task 8:")

capitals = {"Ukraine": "Kiev",
            "USA": "Washington",
            "Poland": "Warsaw",
            "United Kingdom": "London"}
print(*capitals)

while True:
    n = input("Enter name of country: ")
    if n in capitals:
        print(capitals[n])
        break
    else:
        print("We don`t have that country")

print("Extra task:")
list_5 = [11, 23, 36]
for i, n in enumerate(list_5):
    print(i, n)