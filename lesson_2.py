from dataclasses import replace

str_1 = "type string"
print(type(str_1))

num = 5
print(type(num))

bol = True
print(type(bol))

lst = [1, 4, 5, 34, 23]
print(type(lst))

dictionary = {"name": "John", "age": 18}
print(type(dictionary))

tup = (2, 4, 34, 27)
print(type(tup))

non = None
print(type(non))

name = "Tom"
message = "Tom is a cat"
result = num > 10 or name == "Tom"
print(result)

print(name in message)
print(name not in message)


num_str = 125
num_str_1 = str(num_str)
print(type(num_str_1))


message = "Hi, my name is Python"
str_2 = message.replace("y", "0").replace("i", "1")
print(str_2)

split_test = "This is a split test"
split_test = split_test.split()
print(split_test)

string_join = " ".join(split_test)
print(string_join)

print(len(string_join))

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)

print(list_extend.index(6))

print(len(list_append))

dict_test = {"car" : "Toyota", "price" : 4900, "where" : "EU"}
print(dict_test.get("car"), dict_test.get("where"))
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())