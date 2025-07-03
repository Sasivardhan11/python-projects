#compound Interest calculator
principle = 0
rate = 0
time = 0

while True:
    principle=float(input("Enter the principle amount: "))
    if principle < 0:
        print("principle can't be negative")
    else:
        break

while True:
    rate=float(input("Enter the Interest rate: "))
    if rate < 0:
        print("Interest rate can't be negative")
    else:
        break

while True:
    time=float(input("Enter the time: "))
    if principle < 0:
        print("time can't be negative")
    else:
        break

Balance_amount = principle * (1 + rate/100) ** time
print("The balance amount after",time,"years is",Balance_amount)