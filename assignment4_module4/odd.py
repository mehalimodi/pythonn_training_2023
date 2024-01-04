def get_odd_number():
   while True:
       try:
           number = int(input("Enter an odd number: "))
           if number % 2 == 0:
               raise ValueError("Invalid input. Please enter an odd number.")
           return number
       except ValueError as e:
           print(e)

odd_number = get_odd_number()

print("You entered the odd number:", odd_number)
