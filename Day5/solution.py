# for loop
# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(f"{fruit} pie")
#
# print(fruits)


# max_score
# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
#
# higher_score = 0
#
# for i in student_scores:
#     if higher_score < i:
#         higher_score = i
#
# print(higher_score)

# range()
# num = 0
# for i in range(1, 101):
#     num += i
#
# print(num)

# range() 1-100
# for i in range(1, 101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#
#         print("Buzz")
#     else:
#         print(i)

import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
result = ""

for i in random.choices(range(nr_letters), k=nr_letters):
    result += (letters[i])
print(result)

for i in random.choices(range(nr_numbers), k=nr_numbers):
    result += str(numbers[i])
print(result)

for i in random.choices(range(nr_symbols), k=nr_symbols):
    result += symbols[i]
print(result)
