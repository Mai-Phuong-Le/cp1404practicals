"""shop_caculator"""
total_price = 0
numbers_of_items = int(input("Enter number of items: "))
for i in range(numbers_of_items):
    price_for_each_item = float(input("Enter price for each item: "))
    total_price += price_for_each_item
print(f"Total price for {numbers_of_items} is ${total_price}")