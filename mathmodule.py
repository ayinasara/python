'''
Author:Ayina
18-10-24
Description:Python program that uses functions from the math module to perform the following operations on a number provided by the user:
Expected Output:
Enter a number: 5
Square root of 5: 2.23606797749979
Factorial of 5: 120
5 raised to power 2: 25.0
'''



import math
number=int(input("enter a num"))

square_root=(math.sqrt(number))
print("square root of 5 is ",number,square_root)
factorial=(math.factorial(number))
print("factorial is ",factorial)
power=(math.pow(number,2))
print("5 raised to 2 is",power)