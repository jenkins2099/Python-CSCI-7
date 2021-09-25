weight=int(input("Enter your weight in lbs "))
height=int(input("Enter your height in inches "))
bmi= round((weight/height**2)*703,2)

print("Your BMI is",bmi)

if bmi < 18.5:
    print("You are underweight")
elif bmi >=18.5 and bmi <=24.9 :
    print("You are normal weight")
elif bmi >30:
    print("You are overweight")
else:
    print("You are obese")

