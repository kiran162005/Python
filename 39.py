# Python Banking Program

def show_balance(balance):
    print("**************************")
    print(f" Your balance is: {balance:.2f} ")
    print("**************************")


def deposit():
    print("**************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("**************************")

    if amount < 0:
        print("This is not a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    print("**************************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("**************************")

    if amount > balance:
        print("Insufficient funds")
        return 0
