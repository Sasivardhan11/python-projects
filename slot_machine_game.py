#Slot Machine Game
import random,time

def spin_row():
    symbols = ['🍉', '🍒','⭐','🔔','🍋']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet *10
        elif row[0] == '⭐':
            return bet *20
        elif row[0] == '🔔':
            return bet *5
        elif row[0] == '🍋':
            return bet *4
        elif row[0] == '🍒':
            return bet *3
    return 0

def main():

    print("****************************")
    print("Welcome to Slot Machine Game")
    print("Symbols are 🍉🍒⭐🔔🍋")
    print("****************************")

    balance = 100

    while balance > 0:
        print(f"Your Current Balance : ${balance:.2f}")
        bet = input("Enter Your bet amount : ")

        if not bet.isdigit():
            print("Enter a valid bet amount!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficent Funds!")
            continue
        if bet <= 0:
            print("Bet should br greater than 0!")
            continue

        balance -= bet

        row = spin_row()

        print("Spinning....")
        time.sleep(1)
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry You lost this round!")
        
        balance += payout
        
        spin_again = input("You want to spin again (Y/N) : ").upper()

        if spin_again != 'Y':
            break
    print("********************************")
    print(f"Your Final Balance is ${balance}")
    print("Have a nice day! visit again!")
    print("********************************")
if __name__ == "__main__":
    main()