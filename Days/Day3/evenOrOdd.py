#Check if number user inputs is Even or Odd
number=int(input('Enter the number you want to check '))
numCheck=number%2
if numCheck==0:
    print('Your number is Even')
else:
    print('Your number is Odd')
