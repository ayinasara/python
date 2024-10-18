'''
Author:Ayina
18-10-24
Description:program that demonstrates the usage of arithmetic, comparison, and logical operators
Expected Output:
Sum: 15, Division: 2.0
Is a greater than b?: True
Are a and b equal?: False
Logical AND: True
Logical OR: True
'''


num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

print("Sum=",num1+num2,",division=",num1/num2)
print("Is num1 greater than num2?:",num1>num2)
print("Are num1 and num2 equal?:",num1==num2)
print( "LogicaL AND:",num1>0 and num2>0)
print("Logical OR:",num1>5 or num2<5)
