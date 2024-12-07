'''
-1 for water 
0 for gun
1 for snake
'''

import random

computer = random.choice([-1, 0 ,1])
Your_choice = input("Enter a choice: ")
Main_Dict ={ "s" : 1, "g" : 0, "w": -1}
Reverse_Dict = {1 : "Snake", 0 : "Gun", -1 : "Water"}
you = Main_Dict[Your_choice]

print(f"You chose {Reverse_Dict[you]}\nComputer chose {Reverse_Dict[computer]}")

if(computer == you):
    print("It's a DRAW !")
else:
    if(computer == -1 and you == 1):
        print("You WIN !")
    elif(computer == -1 and you == 0):
        print("You LOSE !")
    elif(computer == 0 and you == -1):
        print("You WIN !")
    elif(computer == 0 and you == 1):
        print("You LOSE !")
    elif(computer == 1 and you == -1):
        print("You LOSE !")
    elif(computer == 1 and you == 0):
        print("You WIN !")
    else:
        print("Something went wrong !")

# Shortened Logic(Just for explaination)
'''if((computer - you) == -1 or  (computer - you) == 2 ):
        print("You lose!")
    else:
        print("You win!") '''





