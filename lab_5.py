balance_amount=1000
while True:
    print("\n1.\tCheck Balance")
    print("2.\tDeposit money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("enter your choice:"))

    if choice==1:
        print(f"the current balance$ {balance_amount}")

    elif choice==2:
        deposit_amount=float(input("enter amount "))
        balance_amount=balance_amount+deposit_amount
        print(f"the deposited amount${deposit_amount} and the current balance${balance_amount}")
    elif choice==3:
        withdraw_amount=float(input("enter the amount to be withdrawn"))
        if withdraw_amount>balance_amount:
            print("insufficient balance")
        else:
            balance_amount = balance_amount - withdraw_amount


        print(f"the amount withdrawn from the account{withdraw_amount} and "f"the balance amount{balance_amount}")


    elif choice==4:
        break
    else:
        print("invalid entry")