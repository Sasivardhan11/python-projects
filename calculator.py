operator = input("select a operator (+,-,*,/) : ")
num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print(f"{operator} is not a valid operator")