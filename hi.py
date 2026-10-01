band = input("Enter the band name: ")
num_people = int(input("Enter the number of people: "))
ticket_price = float(input("Enter the ticket price: "))


def show_cost(band_name, people, price):
    total_cost = people * price
    print(f"Band: {band_name}")
    print(f"Number of people: {people}")
    print(f"Ticket price: ${price:.2f}")
    print(f"Total cost: ${total_cost:.2f}")


show_cost(band, num_people, ticket_price)
