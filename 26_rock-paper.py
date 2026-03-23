import random

options = ("rock", "paper", "scissors")
running = True

while True:

    player = None
    computer = random. choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

