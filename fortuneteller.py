import random


def get_number(prompt, number_type):
    while True:
        try:
            user_input = input(prompt)
            if number_type is int:
                return int(user_input)
            elif number_type is float:
                return float(user_input)
            else:
                raise TypeError("Unsupported number type.")
        except ValueError:
            print("That is not a valid number. Please try again.")
        except TypeError:
            print("Type error. Please enter a valid number.")


def fortune_teller():
    print("Welcome traveler. The mystic fortune teller is ready to read your fate.")
    print("Answer with numbers and the stars will reveal your destiny.")

    lucky_number = get_number("Enter your lucky number: ", int)
    years_ahead = get_number("How many years into the future do you want to look? ", float)
    magical_multiplier = get_number("Enter a magical multiplier: ", float)
    moonlight = get_number("How many moonlit points do you see in the sky? ", float)
    destiny_score = get_number("Enter your destiny score as a whole number: ", int)

    random_oracle = random.randint(1, 100)
    fortune_total = lucky_number + years_ahead + magical_multiplier + moonlight + destiny_score + random_oracle

    print("\nThe fortune teller closes their eyes and whispers...")

    if fortune_total < 50:
        fortune = "A quiet path will open before you. You will find wisdom in patience and success in small, steady steps."
    elif fortune_total < 80:
        fortune = "A new opportunity will arrive when you least expect it. Be brave enough to take the first step."
    elif fortune_total < 110:
        fortune = "Your luck is growing. A hidden door will open, revealing a chance that changes your future."
    elif fortune_total < 140:
        fortune = "A powerful ally will appear to guide you. Trust your intuition and believe in your own strength."
    elif fortune_total < 170:
        fortune = "The stars favor bold choices. A bold act of courage will carry you toward a remarkable future."
    elif fortune_total < 200:
        fortune = "A long journey is ahead, but each challenge will sharpen your mind and heart. Victory waits at the end."
    elif fortune_total < 230:
        fortune = "Love and prosperity are closer than you think. Keep your kindness alive and doors will open for you."
    elif fortune_total < 260:
        fortune = "A mysterious gift is coming your way. It may arrive as a lesson, a friendship, or a surprising chance."
    elif fortune_total < 290:
        fortune = "Your future shines brightly. Your hard work will soon be rewarded, and your dreams are within reach."
    else:
        fortune = "You are destined for greatness. The universe has marked you for success, adventure, and unforgettable joy."

    print(f"Calculated fate number: {fortune_total}")
    print(fortune)


if __name__ == "__main__":
    fortune_teller()

#i used ai for the dialogue because i couldnt think of what to put.