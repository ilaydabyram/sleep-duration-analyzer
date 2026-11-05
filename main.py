# Sleep Duration Analyzer

sleep_hours = []

print("Welcome to the Sleep Duration Analyzer!")
print("Enter your sleep duration for 7 days.\n")

for day in range(1, 8):
    hours = float(input(f"Day {day} - How many hours did you sleep? "))
    sleep_hours.append(hours)

average_sleep = sum(sleep_hours) / len(sleep_hours)

longest_sleep = max(sleep_hours)
shortest_sleep = min(sleep_hours)

print("\n--- Sleep Analysis Results ---")

print(f"Average sleep: {average_sleep:.2f} hours")
print(f"Longest sleep: {longest_sleep} hours")
print(f"Shortest sleep: {shortest_sleep} hours")

if average_sleep < 7:
    print("Your average sleep duration is below 7 hours.")
elif average_sleep <= 9:
    print("Your average sleep duration is within the recommended range.")
else:
    print("Your average sleep duration is above 9 hours.")

print("\nDaily Sleep Report:")

for day, hours in enumerate(sleep_hours, start=1):
    print(f"Day {day}: {hours} hours")
