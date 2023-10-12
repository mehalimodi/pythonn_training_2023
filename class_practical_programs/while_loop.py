'''i=1 #initalization
while i<=5: #condition
    print(i)
    i+=1'''

# example 2 
'''status=True
while status:
    name = input("Enter student name:")
    choice = input("Do you want to add more student name : press ' y ' for yes and ' n ' for no:")
    if choice == 'y' or choice == 'Y' or choice == 'Yes':
        status = True
    else:
        status = False'''

# example 3 number guessing game
import random
status = True

computer=random.randint(1,100) #it will give random number
while status:
    user=int(input("Enter your guess:"))
    if user>computer:
        print("HINT: Guess lower number:")
    elif user<computer:
        print("HINT: Guess upper number:")
    else:
        print("your guess is correct:")
        status=False
