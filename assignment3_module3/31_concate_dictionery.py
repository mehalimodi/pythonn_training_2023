# Write a Python script to concatenate following dictionaries to create a new one.
a={'python':60,'java':56,'.net':79}
b={'maths':76,'english':84,'science':93}
dict={}
for d in (a, b): 
    dict.update(d)
print(dict)




