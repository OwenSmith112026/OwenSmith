# Event Planning Report

event_name = input("What is the event name? ")
host_name = input("Who is the host? ")
location = input("Where is the event located? ")
month = input("What month is the event in? ")
day = int(input("What day is the event on? "))

guest_count = int(input("How many guests are attending? "))
table_count = int(input("How many tables are needed? "))
chair_count = int(input("How many chairs are needed? "))
food_budget = float(input("What is the food budget? "))
decoration_budget = float(input("What is the decoration budget? "))

start_time = input("What time does the event start? ")
end_time = input("What time does the event end? ")
first_activity = input("What is the first activity? ")
second_activity = input("What is the second activity? ")
closing_activity = input("What is the closing activity? ")

system32_path = r"C:\Windows\System32"


print("\nEvent Planning Report")
print("=" * 24)

print("\nEvent Details")
print(f"Event Name: {event_name}")
print(f"Host Name: {host_name}")
print(f"Location: {location}")
print(f"Month: {month}")
print(f"Day: {day}")

print("\nGuest and Setup Information")
print(f"Guest Count: {guest_count}")
print(f"Table Count: {table_count}")
print(f"Chair Count: {chair_count}")
print(f"Food Budget: ${food_budget:.2f}")
print(f"Decoration Budget: ${decoration_budget:.2f}")

print("\nSchedule")
print(f"Start Time: {start_time}")
print(f"End Time: {end_time}")
print(f"First Activity: {first_activity}")
print(f"Second Activity: {second_activity}")
print(f"Closing Activity: {closing_activity}")

del system32_path
