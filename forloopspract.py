print("Countdown:")
for number in range(10, 0, -1):
    print(number)

numbers = [3, 7, 12, 4, 9, 15, 2, 8, 6, 11]
total = 0
for number in numbers:
    total += number
print("Sum of the list:", total)

values = [1, 2, 3, 4, 5]
squares = []
for number in values:
    squares.append(number ** 2)
print("Squares:", squares)

text = input("Enter a string: ")
vowel_count = 0
for character in text:
    if character.lower() in "aeiou":
        vowel_count += 1
print("Number of vowels:", vowel_count)

table_number = int(input("Enter a number for its multiplication table: "))
for multiplier in range(1, 11):
    print(f"{table_number} x {multiplier} = {table_number * multiplier}")

names = ["Alice", "Bob", "Charlie"]
print("Greetings:")
for name in names:
    print(f"Hello, {name}!")