limit=int(input("enter the limit"))
number=int(input("enter the number"))
big=number
second_big=int(0)
second_small=int(0)


small=number
while limit>1:
    number=int(input("enter the number"))
    if number>big:
        second_big=big
        big=number
    elif number>second_big:
        second_big=number

    if number<small:
        second_small=small
        small=number

    elif number<second_small:
        second_small=number

    limit=limit-1
print(f"big{big}")
print(f"small {small}")
print(f"second_big{second_big}")
print(second_small)











