string=input("enter string:")
if len(string)>=2:
    if string[:1] == string[-1:]:
        count=len(string)
        print("first and last is same:",count)
    else:
        print("not same")


