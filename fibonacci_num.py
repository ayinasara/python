def fib_numbers(number):

    next_num=0
    nex_1=1
    fibonacci=[0]

    for num in range(number-1):
        fibonacci.append(nex_1)
        next_num,nex_1=nex_1,next_num+nex_1
    print(fibonacci,"fibonacci sequence")

num=int(input("enter number"))
fib_numbers(num)
