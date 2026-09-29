num_apples = int(input("How many apples: "))
num_people = int(input("How many people: "))


def portion_calc(apples, people):
    apples_per_person = apples / people
    return apples_per_person


def serve(people, apples_per_glass):
    print(f"Serving {people} people a glass of apple juice. It takes {apples_per_glass} apples per glass.")


calculated_portion = portion_calc(num_apples, num_people)

serve(num_people, calculated_portion)
