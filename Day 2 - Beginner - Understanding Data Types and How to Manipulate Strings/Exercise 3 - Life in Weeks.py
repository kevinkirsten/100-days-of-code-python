age = input("What is your current age?")
age_int = int(age)
difference_in_years = 90 - age_int
difference_in_days = difference_in_years * 365
difference_in_weeks = difference_in_years * 52
difference_in_months = difference_in_years * 12
print(f"You have {difference_in_days} days, {difference_in_weeks} weeks, and {difference_in_months} months left.")
