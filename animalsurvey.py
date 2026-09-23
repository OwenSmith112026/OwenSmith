
print("--- Welcome to the Animal Survey! ---")
favorite_animal = input("What is your favorite animal? > ")
reason = input("Why is this your favorite animal? > ")
habitat = input("Where do they live? > ")
fun_fact = input("What is a fun fact about them? > ")
color = input("What color are they? > ")


print("\n--- Survey Summary ---")
summary = f"Your favorite animal is the {favorite_animal} because {reason}. " \
          f"They live in {habitat}, and {fun_fact}. " \
          f"They are {color}."


print(summary)
