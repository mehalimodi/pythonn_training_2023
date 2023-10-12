status=True
result=""
while status:
    for i in range(1,6):
        marks=int(input("Enter your marks:"))
        if marks>35:
            result="pass"
            print("pass")
        else:
            result="fail"
            print("fail")
            break
    name=input("Enter your name:")
    print(f"{name} your result is {result}")
    choice=input("do you want to enter more student details:").upper()
    if choice=='N':
        status=False

