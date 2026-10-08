correct_password = "secret123"

while True:
    password = input("Enter your password: ")

    if password == correct_password:
        print("ACCESS GRANTED")
        break
    else:
        print("DENIED")
