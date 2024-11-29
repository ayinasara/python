'''
program to find the factorial of a number
'''

def factorial(num):

    if num==0:
        return 1
    else:
        return(num*factorial(num-1))
num = int(input("enter the number"))
print("factorial of ",num ,"is ",factorial(num))
