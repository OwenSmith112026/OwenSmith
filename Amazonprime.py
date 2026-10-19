age = int(input("age: "))

if age < 18:
    parent_consent = input("Do you have parent consent (yes/no): ").lower()
else:
    parent_consent = "yes"

balance = float(input("Enter your bank account balance: "))
buy_now = input("Do you want to buy (yes/no): ").lower()

if (age >= 18 or parent_consent == "yes") and balance >= 139.99 and buy_now == "yes":
    print("You can buy it.")
else:
    print("You cant buy it.")
