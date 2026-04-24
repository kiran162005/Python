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
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************************")
        print("          Banking Program        ")
        print("*********************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************************")

