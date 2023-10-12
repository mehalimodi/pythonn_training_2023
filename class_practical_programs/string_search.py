'''search=input("enter your string: ")
if search.startswith("https://www.") or search.startswith("http://www."):
    print("searching")
else:
    if search.endswith(".com"):
        print("searching...")
    else:
        s= "https://www." +search+ ".com"
        print(f"{s} searching.......")'''



# string indexing
'''s1="welcome"
print(s1)
print(s1[0])
print(s1[-1])
print(s1[2:5])
'''
# check whether the string available o not

'''s1="my favourate subject is python"
subject=input("entre the subject: ").lower()
if subject in s1:
    print("available")
else:
    print("not available")'''



# count the length of the string
'''s1="hello"
print(len(s1))
print(s1)
count=0
for i in s1:
    # print(i)
    count=count+1
print("len=", count)'''


# 
'''s1="hello"
s2="welcome"

# fetch strting 2 characters for string
print(s1[:2])

# fetch last 2 characters from string
print(s1[-2:])
print(s1[-2:-1])

# 
s3=s1[:2] + s2[-2:]
print(s3)
s3=s1[:2] + "good" + s2[-2:]
print(s3)'''

name="hfh"
print(name.isalpha())

name="664"
print(name.isalpha())

name="67656"
print(name.isdigit())

name="76hgg"
print(name.isdigit())
print(name.isalnum())


















