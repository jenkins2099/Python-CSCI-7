#A love calculator that uses how many times the letters in "true" and "love" appears in the names user inputs
print('Welcolme to the Love Calculator!')
name1=input('What is your name \n')
name2=input('What is their name \n')
combined_names=(name1+name2).lower()
t=combined_names.count("t")
r=combined_names.count("r")
u=combined_names.count("u")
e=combined_names.count("e")
l=combined_names.count("l")
o=combined_names.count("o")
v=combined_names.count("v")
e2=combined_names.count("e")

love_score1=t+r+u+e
love_score2=l+o+v+e2
love_total=int(str(love_score1)+str(love_score2))
print(love_total)

if int(love_total)<10 or int(love_total)>90:
    print(f'Your score is {love_total}, you go together like coke and mentos.')
elif int(love_total)>=40 and int(love_total)<=50:
    print(f'Your score is {love_total}, you are alright together.')
else:
    print(f'Your score is {love_total}')
    
