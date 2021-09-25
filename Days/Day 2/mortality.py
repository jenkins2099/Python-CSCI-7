#Return the time user has left to live in days, weeks, and months if they were to live to 90
age=int(input("What is your current age? "))

age_left_years=90-age
age_left_months=age_left_years*12
age_left_weeks=age_left_years*52
age_left_days=age_left_years*365

if age_left_years > 90:
    print("You've lived a long life.")
else: 
    print(f"You have {age_left_days} days, {age_left_weeks} weeks, and {age_left_months} months left to live.")
