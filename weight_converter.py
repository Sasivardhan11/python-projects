#weight converter
weight = float(input("enter your weight : "))
unit = input("kg or lbs : ")

if unit.lower()=="kg":
    weight = weight * 2.205
    unit = "lbs."
    print(f"your weight is {weight} {unit}")
elif unit.lower()=="lbs":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"your weight is {weight} {unit}")
else:
    print(f"{unit} is not a valid unit")