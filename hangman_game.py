from wordslist import words,hangman_art
import random


def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
      print(line)
    print("***********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(f"Answer is {answer}")

def main():
    answer = random.choice(words)
    hint = ["_"]* len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
      print("*********")
      print("Guess the Word!")
      display_man(wrong_guesses)

      display_hint(hint)
      guess = input("Enter a Letter : ").lower()

      if not guess.isalpha() or len(guess) != 1:
        print("Enter a valid letter!")
        continue
      
      if guess in guessed_letters:
        print(f"{guess} is already guessed")
        continue

      guessed_letters.add(guess)

      if guess in answer:
        for i in range(len(answer)):
          if answer[i] == guess:
            hint[i] = guess
      else:
        wrong_guesses +=1
      
      if "_" not in hint:
        display_man(wrong_guesses)
        display_hint(hint)
        display_answer(answer)
        print("You Win!")
        is_running = False
      elif wrong_guesses >= len(hangman_art)-1:
        display_man(wrong_guesses)
        display_hint(hint)
        display_answer(answer)
        print("You Lose!")
        is_running = False

if __name__ == "__main__":
    main()