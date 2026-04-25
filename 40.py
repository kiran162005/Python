# Python Slot machine

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results


