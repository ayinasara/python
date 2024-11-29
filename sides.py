def check_right_angle():


    side_1=int(input('enter the length of the first side'))
    side_2=int(input("Enter the length of the second side"))
    side_3=int(input("enter the length of the third side"))
    side=[side_1,side_2,side_3 ]
    print(side)
    side.sort()
    print(side)
    if side[2]**2==side[0]**2+side[1]**2:
        print("this is a right triangle")
    else:
        print("this is not a right triangle")


check_right_angle()

