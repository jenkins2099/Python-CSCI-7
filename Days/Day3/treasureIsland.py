#CYOA where user's goal is to reach treasure
print('Welcolme to Treasure Island. /n Your mission is to find the treasure.')
roadChoice=input('You\'re at a cross road. Where do you want to go? Type "left" or "right". ')

if roadChoice=='left':
    lakeChoice=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if lakeChoice=='wait':
        doorChoice=input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one brown. Which colour do you choose? Type "red" for red, "yellow", and "brown" for brown. ')
        if doorChoice=='red':
            print('It\'s a room full of fire. Game Over.')
        elif doorChoice=='brown':
            print('You enter a room full of beasts. Game Over.')
        else:
            print('You found the treasure! You Win!')
    else:print('You get attacked by an angry trout. Game Over.')
else:
    print('You fell into a hole. Game Over.')
    

