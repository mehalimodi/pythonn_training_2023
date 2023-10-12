name=input("Enter your name:")
gender=input("Enter your gender:")
age=int(input("Enter you age:"))
print("your name:",name)
print("your gender:",gender)
print("your age is:",age)
print("---------------------------------------------------------------")

current_price=5752
making_charge=845
print("current gold price (1 gram):",current_price)
print("---------------------------------------------------------------")
status=True
net=0
count=0
while status:
    prod=input("Enter your product:")
    prod_gram=int(input("Enter product gram:"))
    product=1
    total_gold_rate=prod_gram*current_price
    print("total gold rate is:",total_gold_rate)
    print("making charges:",making_charge)
    total_making_charges=prod_gram*making_charge
    print("total making charges is:",total_making_charges)
    print("---------------------------------------------------------------")
    prod_amount=total_gold_rate+total_making_charges
    print("total amount is: ",prod_amount)
    dis=1
    if gender=="male" and age>65:
        if prod_amount>=200000 and prod_amount<=300000:
            print("your discount is 20%:")
            dis=20
        elif prod_amount>=310000 and prod_amount<=500000:
            print("your discount is 30%:")
            dis=30
        elif prod_amount>510000 :
            print("your discount is 35%:")
            dis=35
    if gender=="male" and age<65:
        if prod_amount>=200000 and prod_amount<=300000:
            print("your discount is: 10%")
            dis=10
        elif prod_amount>=310000 and prod_amount<=500000:
            print("your discount is: 20%")
            dis=20
        elif prod_amount>510000 :
            print("your discount is: 30%")
            dis=30
    if gender=="female" and age>65:
        if prod_amount>=200000 and prod_amount<=300000:
            print("your discount is 25%:")
            dis=25
        elif prod_amount>=310000 and prod_amount<=500000:
            print("your discount is 35%:")
            dis=35
        elif prod_amount>510000 :
            print("your discount is 40%:")
            dis=40
    if gender=="female" and age<65:
        if prod_amount>=200000 and prod_amount<=300000:
            print("your discount is: 15%")
            dis=15
        elif prod_amount>=310000 and prod_amount<=500000:
            print("your discount is: 25%")
            dis=25
        elif prod_amount>510000 :
            print("your discount is: 30%")
            dis=30

    discount=0
    discount=(total_gold_rate*dis)/100
    print("discount is:",discount)
    print("---------------------------------------------------------------")
    net_amount=prod_amount-discount
    print("total amount of gold is:",net_amount)
    new_item=input("do you want to add more item? Press 'Y' or ' N ': ")
    if new_item=='y':
        status=True
    else:
        status=False
    count+=product
    net+=net_amount
print("total of all items:",net)
print("you have selected :",count)
