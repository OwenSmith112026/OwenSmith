# Quiz program with a score tally

# Question 1
answer1 = input("1. What is 2 + 2? ")

# Question 2
answer2 = input("2. What color is the sky on a clear day? ")

# Question 3
answer3 = input("3. How many sides does a triangle have? ")

# Question 4
answer4 = input("4. Which planet is known as the Red Planet? ")

# Question 5
answer5 = input("5. What is 10 / 2? ")


def tally_score(a1, a2, a3, a4, a5):
    score = 0

    if a1.strip().lower() == "4":
        score += 1

    if a2.strip().lower() == "blue":
        score += 1

    if a3.strip().lower() == "3":
        score += 1

    if a4.strip().lower() == "mars":
        score += 1

    if a5.strip().lower() == "5":
        score += 1

    print(f"Your score is {score}/5")


# Call the function and pass the five answers
# This checks each answer and tells the user their total score.
tally_score(answer1, answer2, answer3, answer4, answer5)
