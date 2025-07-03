# Banking Program
import time

def show_balance(balance, c_pin):
    try:
        if c_pin == int(input("Enter Your pin : ")) :
            print("---------------------------")
            print(f"Your account balance is : ${balance:.2f}")
            print("---------------------------")
        else:
            print("You have entered wrong pin number.")
            print("---------------------------")
    except ValueError:
        print("Invalid pin input.")
        print("---------------------------")


def deposit(c_pin):
    try:
        if c_pin == int(input("Enter Your pin : ")) :
            while True:
                print("---------------------------")
                amount = float(input("Enter the amount to deposit : "))
                print("---------------------------")
                if amount < 0:
                    print("Not a valid Amount!")
                    print("---------------------------")
                else:
                    print(f"Your account has credited ${amount:.2f}")
                    print("Transaction successful!")
                    print("---------------------------")
                    return amount
        else:
            print("You have entered wrong pin number.")
            print("---------------------------")
            return 0
    except ValueError:
        print("Enter Valid Amount!")
        print("---------------------------")
        return 0


def withdraw(balance, c_pin):
    try:
        if c_pin == int(input("Enter Your pin : ")) :
            while True:
                print("---------------------------")
                amount = float(input("Enter the amount to withdraw : "))
                print("---------------------------")
                if amount > balance:
                    print("Insufficient balance!")
                    print(f"Account Balance : ${balance:.2f}")
                    print("---------------------------")
                    return 0
                elif amount < 0:
                    print("Enter valid amount!")
                    print("---------------------------")
                else:
                    print(f"Your account has debited ${amount:.2f}")
                    print("Transaction successful!")
                    print("---------------------------")
                    return amount
        else:
            print("You have entered wrong pin number.")
            print("---------------------------")
            return 0
    except ValueError:
        print("Enter a Valid Amount!")
        print("---------------------------")
        return 0


def set_pin():
    while True:
        try:
            return int(input("Choose Your Account Pin : "))
        except ValueError:
            print("Please Enter a Valid pin number!")


def reset_pin(current_pin):
    try:
        if current_pin == int(input("Enter Your current Pin : ")):
            return int(input("Choose your new pin : "))
        else:
            print("You entered wrong pin.")
            print("---------------------------")
            return current_pin
    except:
        print("Please Enter valid pin number!")
        print("---------------------------")
        return current_pin


def main():
    balance = 0.0
    is_running = True
    current_pin = set_pin()

    try:
        if int(input("Enter your pin to access the account: ")) == current_pin:
            while is_running:
                time.sleep(1)
                print("---------------------------")
                print("Banking Program")
                print("---------------------------")
                print("1. Show Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Reset Pin")
                print("5. Exit")
                print("---------------------------")
                choice = input("Enter your option (1-5) : ")
                print("---------------------------")
                if choice == '1':
                    show_balance(balance, current_pin)
                elif choice == '2':
                    balance += deposit(current_pin) or 0
                elif choice == '3':
                    balance -= withdraw(balance, current_pin) or 0
                elif choice == '4':
                    current_pin = reset_pin(current_pin)
                elif choice == '5':
                    print("Thank You!")
                    time.sleep(1)
                    is_running = False
                else:
                    print("Enter a Valid Choice!")
                    print("---------------------------")
            print("Have a nice day!")
        else:
            print("You have entered wrong pin number!")
    except ValueError:
        print("Invalid pin format!")

if __name__ == "__main__":
    main()