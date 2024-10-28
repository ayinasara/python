
while True:
    print("1\t convert celsius to fahrenheit")
    print("2\t convert fahrenheit to celsius")
    print("3\t exit the program")
    choice=int(input("enter your choice"))
    if choice==1:
        tem=float(input("enter temperature in celsius"))
        tem1=(tem*9/5)+32
        print(tem1,",temperature in fahrenheit")
    elif choice==2:
        tem=float(input("enter temperature in fahrenheit"))
        tem2=(tem-32)*5/9
        print(tem2,",temperature in celsius")
    elif choice==3:
        break

    else:
        print("invalid option")

