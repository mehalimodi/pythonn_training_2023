import random

game_list=["rock","paper","scissor"] #creating list
flag=True
while flag:
    computer=random.choice(game_list)
    user=input("choose rock / paper / scissor:")
    if user==computer:
       print("tie")
    elif user=="rock" and computer=="scissor":
        print("user won this game")
    elif user=="rock" and computer=="paper":
        print("computer won this game")
    elif user=="paper" and computer=="scissor":
        print("computer won this game")
    elif user=="scissor" and computer=="paper":
        print("user won this game")
    elif user=="scissor" and computer=="rock": 
        print("computer won this game")
    elif user=="paper" and computer=="rock":
        print("user won this game")
        print(computer)
    print("computer input is:",computer)

    flag=False