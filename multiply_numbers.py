'''
product of two numbers using recursion
'''

def recursivemultiply(num1,num2):


    if num2==1:
        return num1
    else:
        return num1+recursivemultiply(num1,num2-1)
num_1=int(input("enter number1"))
num_2=int(input("enter number 2"))
print("the product of two numbers" ,num_1,"and",num_2,"is", recursivemultiply(num_1,num_2))