import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("The word was:", answer)

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    max_wrong = 6

    print("Welcome to Hangman!")

    while True:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} already guessed")
            continue
        
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        # Win condition
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN 🎉")
            break

        # Lose condition
        if wrong_guesses >= max_wrong:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE 💀")
            break

if __name__ == "__main__":
    main()