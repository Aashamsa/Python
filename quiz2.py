print("---------")
print("WELCOME!")
print("---------")
questions = {"What is the capital of Italy?" : "A. Rome",
             "What is the closest planet to the sun?" : "B. Mercury",
    "How many bones are there in a human body?" : "D. 206",
    "How many alphabets are in the english language?" : "B. 26"
}
options = (("A. Rome", "B. Paris", "C. Berlin","D. Venice"),
           ("A. Earth", "B. Mercury", "C. Venus", "D. Saturn"),
           ("A. 203", "B. 209", "C. 200", "D. 206"),
           ("A. 20", "B. 26", "C. 29", "D. 30"))
question_num = 0
score = 0
guesses = []
answers = ("A", "B", "D", "B")
for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A/B/C/D): ").upper()
    guesses.append(guess)
    if guess ==answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1
print ("--------------")
print("RESULTS")
print("--------------")
print("answers: ", end="")
for answer in answers:
    print(answer, end = " ")
print()
score = int (score / len(questions) * 100)
print(f'Your score is : {score}%')