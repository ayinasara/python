'''
description:Python program to find the largest of three numbers.
date:25-10-24
'''


num1=input("enter first number")
num2=input("enter second number")
num3=input("enter third number")
if num1>num2 and num1>num3:
    print("the largest no is",num1)
elif num2>num3:
    print("the largest no is",num2)
else:
    print("the largest no is",num3)



