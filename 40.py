# Python Slot machine

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results


def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")


def get_payout(row, bet):
    # All 3 match
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = 100

    print("************************")
    print(" Welcome to Python Slots ")
    print("************************")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

    while balance > 0:
        print(f"\nCurrent balance: {balance}")

        bet = input("Enter your bet amount(or 'q' to quit): ")

        if bet.lower() == 'q':
            break

        if not bet.isdigit():
            print("Invalid input")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds ")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("\nSpinning...\n")
        print_row(row)

        winnings = get_payout(row, bet)

        if winnings > 0:
            print(f"You won {winnings}!")
        else:
            print("You lost!")

