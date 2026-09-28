"""shop_caculator"""

total = 0
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9

number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid input")
    number_of_items = int(input("Enter number of items: "))

for i in range(1,number_of_items+1):
    price = float(input("Enter price for each item {i}: $"))
    while price < 0:
        print("Invalid input")
        price = float(input("Enter price for each item {i}: $"))
    total += price

if total > DISCOUNT_THRESHOLD:
    total *= DISCOUNT_RATE

print(f"Total price for {number_of_items} items is ${total:.2f}")