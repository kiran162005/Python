# Python Number guessing game

import random 

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_runnig = True

print("Python number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_runnig:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        