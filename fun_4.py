'''
Write a Python function to multiply all the numbers in a list.
'''

def sum(number):
        multiply= 1

        for x in number:
            multiply*= x
        return multiply

list = []
num_1 = int(input("enter the number"))
num_2 = int(input("enter the number"))
num_3 = int(input("enter the number"))
list.append(num_1)
list.append(num_2)
list.append(num_3)
print(list)
print("sum of three numbers is ", sum(list))
