total_bill=float(input("What was the total bill? "))
bill_split=float(input("How many people are there to split the bill? "))
tip_percentage=float(input("What percentage of tip would you like to give? 10, 12, or 15? "))/100
tip_total=round(float((total_bill/bill_split)*tip_percentage),2)
print(f"Each person should pay ${tip_total}")
