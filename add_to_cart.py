#Your Order
items =[]
count = []
prices = []
totals=[]

while True:

    item= input("Enter your item (q to quit): ")
    if item.lower() == 'q':
        break
    else:
        try:
            num= int(input("Enter the no of items : "))
            price = int(input("Enter the price of the item : "))
        except ValueError:
            print("Please enter valid number for quantity and price")

        items.append(item)
        count.append(num)
        prices.append(price)

print("--------Your Cart--------")

total=0

for i in range(0,len(items)):
    item_total = count[i]*prices[i]
    totals.append(item_total)
    total+=item_total
    print(items[i],count[i],"X",prices[i],":",item_total)

print("-------------------------")

print(f"Grand Total : {total}")