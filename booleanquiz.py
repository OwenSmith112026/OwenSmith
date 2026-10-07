print("Welcome to the Boolean Quiz!")
print("Answer each question with a whole number.")

# Comparison operator questions
answer1 = int(input("Question 1: Give a whole number that is less than 5.\n"))
print(answer1 < 5)

answer2 = int(input("Question 2: Give a whole number that is greater than 10.\n"))
print(answer2 > 10)

answer3 = int(input("Question 3: Give a whole number that is equal to 7.\n"))
print(answer3 == 7)

answer4 = int(input("Question 4: Give a whole number that is less than or equal to 12.\n"))
print(answer4 <= 12)

answer5 = int(input("Question 5: Give a whole number that is greater than or equal to 20.\n"))
print(answer5 >= 20)

# Logical operator questions
answer6 = int(input("Question 6: Give a whole number that is greater than 3 and less than 9.\n"))
print(3 < answer6 < 9)

answer7 = int(input("Question 7: Give a whole number that is less than 0 or greater than 15.\n"))
print(answer7 < 0 or answer7 > 15)

answer8 = int(input("Question 8: Give a whole number that is greater than 5 and less than or equal to 10.\n"))
print(answer8 > 5 and answer8 <= 10)
