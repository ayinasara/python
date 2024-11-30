'''
Write a Python function to find the maximum of three numbers.
'''
def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3:
        return num2
    else:
        return num3
num_1=int(input('enter number1'))
num_2=int(input("enter number2"))
num_3=int(input("enter number3"))
print("max of three numbers is ",maximum(num_1,num_2,num_3))