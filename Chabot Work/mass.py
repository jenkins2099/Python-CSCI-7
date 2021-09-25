#Calculate Weight in newtons but don't give weight if newtons are too high or low

mass=float(input("Enter object's massin kg: "))
weight=round(mass*9.8,2)

if weight > 1000:
    print("The object is too heavy")
elif weight < 10:
    print("The object is too light")
else:
    print(f"The object weighs {weight} newtons")

