#Rock Paper Sciccors Game
import random
import time

options = ("rock","paper","scissors")

#         winner-key  lose-value
points = {"scissors":"paper",
            "rock":"scissors",
            "paper":"rock"}

print("-----------------------------------")
print("Let's Play Rock Paper Scissors Game")
print("-----------------------------------")

is_playing = True

while is_playing:
    print("-----------------------------------")
    print("You have two modes")
    print("1. Computer (C)")
    print("2. Duel Play (D)")
    print("-----------------------------------")

    Mode = input("Select your Mode (C/D) : ").lower()
    if Mode == "c":

        player = None
        computer = random.choice(options)

        try:
            rounds=int(input("Enter Number of rounds you want to play : "))
            while rounds>0:
                player=None
                while player not in options:
                    player = input("Enter you option (rock, paper, scissor): ")
                print(f"your choice: {player}")
                print(f"computer chioce: {computer}")

                if player == computer:
                    print("It's a Tie!")
                elif player in points and points[player] == points.values():
                    print("You Won!")
                else:
                    print("You Lost!")
                rounds-=1

        except ValueError:
            print("Enter valid number!")
        if not input("You want to play again (y/n): ") == 'y':
                is_playing = False

        print("Thankyou for playing!")
    else:
        player1 = input("Enter Player1 Name: ")
        player2 = input("Enter Player2 Name: ")

        player1_options = []
        player2_options = []

        p1_score = 0
        p2_score = 0

        winner=""

        time.sleep(1)

        print(f"{player1} vs {player2}")
        print("-----------------------------------")
        print("---------------RULES---------------")

        items = points.items()
        print("WINNER                 LOSER")
        for key,value in points.items():
            print(f"{key:23}{value}")

        print("-----------------------------------")


        try:
            rounds = input("Enter Number of rounds to be played : ")
            rounds=int(rounds)
            for i in range(0,rounds) :
                player1_options.append(random.choice(options))
                player2_options.append(random.choice(options))
                key = player1_options[i]
                value = player2_options[i]

                time.sleep(2)

                if key == value:
                    print(f"{player1} : {key} X {value} : {player2}")
                    print("Match Tie")
                    continue
                elif key in points and points[key] == value:
                    print(f"{player1} : {key} X {value} : {player2}")
                    print(f"{player1} Won!")
                    p1_score+=1
                else:
                    print(f"{player1} : {key} X {value} : {player2}")
                    print(f"{player2} Won!")
                    p2_score+=1
            time.sleep(1)
            print(f"{player1} options are : {player1_options}")
            print(f"{player2} options are : {player2_options}")
            print(f"{player1} score is : {p1_score}")
            print(f"{player2} score is : {p2_score}")

            if p1_score != p2_score:
                if p1_score> p2_score:
                    winner=player1
                else:
                    winner = player2

                print("-----------------------------------")
                print(f"The Winner is {winner}")
            else:
                print("-----------------------------------")
                print("Scores are equal")
                print("Let's play one more time")

            if not input("You want to play again (y/n): ") == 'y':
                is_playing = False
            print("Thankyou for playing!")
        except ValueError:
            print("Invalid Input Number")
