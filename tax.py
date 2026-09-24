def calculate_tax(item, price, rate):
    tax_amount = price * (rate / 100)
    total_price = price + tax_amount
    
    print(f"{item} costs ${price:.2f} dollars before tax and ${total_price:.2f} after tax.")

user_item = input("Enter the name of the item: ")
user_price = float(input("Enter the cost of the item in dollars: "))
user_rate = float(input("Enter the tax rate (e.g., enter 6.875 for Minnesota): "))

calculate_tax(user_item, user_price, user_rate)

