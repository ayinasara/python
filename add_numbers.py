


def recursiveadd(num1,num2):


    if num2==0:
        return num1
    else:
        return recursiveadd(num1+1,num2-1)
num_1=int(input("enter number1"))
num_2=int(input("enter number 2"))
print("the sum of two numbers" ,num_1,"and",num_2,"is", recursiveadd(num_1,num_2))

