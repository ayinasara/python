def sum(number):
    sum_1 = 0

    for x in number:
        sum_1 += x
    return sum_1
list=[]
num_1=int(input("enter the number"))
num_2=int(input("enter the number"))
num_3=int(input("enter the number"))
list.append(num_1)
list.append(num_2)
list.append(num_3)
print(list)
print( "sum of three numbers is ",sum(list))




