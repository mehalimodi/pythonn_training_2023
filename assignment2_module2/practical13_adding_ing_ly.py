string=input("enter the string:")
length=len(string)
if length>=3:    
    if string[-3:]=='ing':
        new=string+'ly'
        print(new)
    else:
        new=string+'ing'
        print(new)
else:
    print("will not change:",string)