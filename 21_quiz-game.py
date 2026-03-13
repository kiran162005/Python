#Python quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in humnn body?: ",
             "Which planet in the solar system is the hottes?: ")

options = (("A. 116", "B. 117 ", "C. 118 ", "D. 119 "), 
           ("A. Whale", "B. crocodile", "C. Elephant", "D. ostrich "), 
           ("A. Nitrogen", "B. Oxygen", "C. carbon-Dioxide", "D. Hydrogen "), 
           ("A. 206", "B. 207 ", "C. 208", "D. 209"), 
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


