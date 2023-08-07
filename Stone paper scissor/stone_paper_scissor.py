def gamewin(Computer,palyer):
    if player==Computer:
        return "Draw"
    elif Computer=="s":
        if player=="p":
            return True
        elif player=="sc":
            return False
    elif(Computer=="p"):
        if player=="s":
            return False
        elif(player=="sc"):
            return True

    elif(Computer=="sc"):
        if player=="p":
            return False
        elif(player=="s"):
            return True
        

import random
random_no=random.randint(1,3)
print(random_no)
if random_no==1:
    Computer="s"
elif random==2:
    Computer="p"
elif random==3:
    Computer="sc"
player=input("Play your turn:\n Enter s for stone\n sc for scissor\n p for paper").lower()
result=gamewin(Computer,player)


if result=="Draw":
    print("This game is Draw")
elif result==True:
    print("The player won the game")
elif result==False:
    print("player lose the game")



