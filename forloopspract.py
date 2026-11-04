print("Countdown:")
for i in range(10, 0, -1):
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for number in numbers:
    total = total + number
print("Sum:", total)

numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number * number)
print("Squares:", squares)

word = input("Enter a string: ")
vowels = 0
for letter in word:
    if letter in "aeiouAEIOU":
        vowels += 1
print("Vowels:", vowels)

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Hello,", name + "!")