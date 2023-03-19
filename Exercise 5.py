# Snake Water Gun

# Snake, Water and Gun is a variation of the children's game *rock-paper-
# scissors” where players use hand gestures to represent a snake, water, or
# a gun. The gun beats the snake, the water beats the gun, and the snake
# beats the water.

# Write a python program to create a Snake Water Gun game in Python using
# if-else statements. Do not create any fancy GUI. Use proper functions to
# check for win.

import random
print("0 : Snack, 1 : Water, 2 :Gun ")
validip = [0, 1, 2]
rules =  [['Draw','Win','Loss'], ['Loss','Draw','Win'], ['Win','Loss','Draw']]
play = True
cpscore = 0
ipscore = 0
while play:
    ip = int(input("Enter your choise "))
    if ip not in validip:
        print("Enter valid input")
        break
    cp = random.choice([0, 1, 2])
    print(f"Computer's input {cp}")
    if(rules[ip][cp]=='Win'):
        ipscore += 1
    elif(rules[ip][cp]=='Loss'):
        cpscore += 1
    print(rules[ip][cp])
    play = int(input("Enter 1 to play again 0 to stop game "))

print(f"Player Score {ipscore}") 
print(f"Computer Score {cpscore}") 

if (ipscore > cpscore):
    print("Player Wins")
elif(cpscore > ipscore):
    print("Computer Wins")
else:
    print("Match Drawn")