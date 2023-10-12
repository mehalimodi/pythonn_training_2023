'''subject= "PYTHON"
name=input("Enter you subject name:").upper()
if name==subject:
    print(name)
else:
    print("invalid subject")'''

# example 2 multi line string or document string
menu="""        
                 MENU
            Press 1 for YES
            Press 2 for NO
"""
print(menu)



# try
l1='occurences of substring in a string'
l2='occurences substring'
count=0
sub_length=len(l2)
for i in range(len(l1)):
    if l1[i:i+sub_length]==l2:
        count+=1
print(count)