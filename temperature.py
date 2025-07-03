unit = input("celsius or fahrenheit (c/f): ")
temp = float(input("enter the temperature: "))
if unit.lower() == "c":
    temp = round((9*temp) / 5 + 32, 1)
    print(f"the temperature in fahrenheit is: {temp}°F") 
elif unit.lower() == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"the temperature in celsius is: {temp}°C")
else:
    print(f"{unit} is not a valid unit. Please enter c for celsius or f for fahrenheit.")