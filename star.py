rows=int(input("enter the no of rows"))
print('increasing triangle')
for i in range(1,rows+1):
    for j in range(i):
       print("*" ,end ="\t")
    print()
rows=int(input("enter the no of rows"))
print("decreasing triangle")
for i in range (rows,0,-1):
    for j in range(i):
        print('*',end="\t")
    print()
rows = int(input("enter the no of rows"))
print ("hill pattern")
for i in range(1,rows+1 ):
        for j in range(rows-i):
            print(" ",end="\t")
        for k in range(2*i-1):
               print('*', end="\t")
        print()
rows = int(input("enter the no of rows"))
print("reverse hill pattern")
for i in range( rows,0,-1):
    for j in range(rows - i):
        print(" ", end="\t")
    for k in range(2 * i - 1):
        print('*', end="\t")
    print()
