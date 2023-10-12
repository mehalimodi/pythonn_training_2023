import random
status = True
choice=0
computer=random.randint(1,10) #it will give random number
while status:
    print("do you want hint? press 'y' for hint and 'n' for not:")
    hint=input("hint:")
    if hint=='y':
        print("you ans is:",computer)
    else:
        print("try")
    # life_line=input("do you want life line? press 'y' for yes")
    # if life_line=='y':
    #     print()
    # else:
    #     print()
    user=int(input("Enter your guess:"))
    if user>computer:
        print("HINT: Guess lower number:")
    elif user<computer:
        print("HINT: Guess upper number:")    
    else:
        print("your guess is correct:")
        status=False
        

choice=input("You have completed level 1 , Press : 'y' for next level:")
if choice=='y':
    status=True
    computer=random.randint(1,100) #it will give random number
    while status:
        print("do you want hint? press 'y' for hint and 'n' for not:")
        hint=input("hint:")
        if hint=='y':
            print("you ans is:",computer)
        else:
            print("try")
        user=int(input("Enter your guess:"))
        if user>computer:
            print("HINT: Guess lower number:")
        elif user<computer:
            print("HINT: Guess upper number:")
        else:
            print("your guess is correct:")
            status=False

choice=input("You have completed level 2 , Press : 'y' for next level:")
if choice=='y':
    status=True
    computer=random.randint(1,300) #it will give random number
    while status:
        print("do you want hint? press 'h' hint and 'n' for not:")
        hint=input("hint:")
        if hint=='y':
            print("you ans is:",computer)
        else:
            print("try")
        user=int(input("Enter your guess:"))
        if user>computer:
            print("HINT: Guess lower number:")
        elif user<computer:
            print("HINT: Guess upper number:")
        else:
            print("your guess is correct:")
            print("you won this game")
            status=False
        


    