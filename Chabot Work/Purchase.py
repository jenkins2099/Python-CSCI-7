itemOne=float(input("Enter the price of your first item "))
itemTwo=float(input("Enter the price of your second item "))
itemThree=float(input("Enter the price of your third item "))
itemFour=float(input("Enter the price of your fourth item "))
itemFive=float(input("Enter the price of your fifth item "))
subtTotalSale=round(itemOne+itemTwo+itemThree+itemFour+itemFive,2)
salesTax=0.07
totalSale=round((subtTotalSale*salesTax)+subtTotalSale,2)
print("Your subtotal is",subtTotalSale)
print("The sales tax is",salesTax)
print("The total of your purchase is",totalSale)

