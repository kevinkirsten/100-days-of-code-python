print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total = bill + total_tip_amount
total_per_person = '{:.2f}'.format(round(total / people, 2))
print(f"Each person should pay: ${total_per_person}")
