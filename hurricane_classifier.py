# Hurricane category classifier

try:
    wind_speed = float(input("Enter wind speed in MPH: "))

    if wind_speed < 74:
        category = "Tropical storm"
    elif wind_speed < 96:
        category = "Category 1"
    elif wind_speed < 111:
        category = "Category 2"
    elif wind_speed < 130:
        category = "Category 3"
    elif wind_speed < 157:
        category = "Category 4"
    else:
        category = "Category 5"

    print(f"The hurricane category is: {category}")

except ValueError:
    print("Invalid input. Please enter a number for wind speed.")
