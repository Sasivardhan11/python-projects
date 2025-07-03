#Number Guessing game
import random

low_num=1
high_num=100
answer= random.randint(low_num,high_num)

guesses=0

is_playing = True

print("Python Number Guessing Game")
print(f"Select the number btw {low_num} and {high_num}")

while is_playing:
    guess = input("Enter your guessing number: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if low_num>guess>high_num:
            print(f"Please select the number btw {low_num} and {high_num}: ")
        elif answer>guess:
            print("Too Low!")
        elif answer<guess:
            print("Too High!")
        else:
            print("Correct!")
            print(f"Your Guesses are {guesses}")
            is_playing = False
    else:
        print("Invalid Guess")
        print(f"Please select the number btw {low_num} and {high_num}: ")
