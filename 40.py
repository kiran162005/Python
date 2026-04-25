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


