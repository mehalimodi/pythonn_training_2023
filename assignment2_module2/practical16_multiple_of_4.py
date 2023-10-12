string=input("enter the string:")
rev_string=len(string)
if rev_string%4==0:
    for i in string[::-1]:
        print(i,end="")
else:
    print(string)
    print("it is not multiple of 4 so it will not reverse")