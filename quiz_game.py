#quiz game

questions = (("what is 2+2 = ?"),
             ("what is 10%2 = ?"),
             ("what is 3-(-3) = ?"),
             ("what is 5*20 = ?"),
             ("what is 33/3 = ?")) 

options = ( ("A. 4" ,"B. 5" ,"C. 6" ,"D. 7"),
            ("A. 0" ,"B. 1" ,"C. 2" ,"D. 3"),
            ("A. 3" ,"B. 9" ,"C. 0" ,"D. 6"),
            ("A. 0" ,"B. 100" ,"C. 50" ,"D. 20"),
            ("A. 3" ,"B. 10" ,"C. 11" ,"D. 20"))

answers = ("A","A","D","B","C")

guesses = []

score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    

    guess=input("Enter your Option (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num+=1

print("--------------------------")
print("         RESULTS          ")
print("--------------------------")

print("answers:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses:",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is : {score}%")