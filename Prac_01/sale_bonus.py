"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales < 0:
    print("Invalid input")
    sales = float(input("Enter sales: $"))
    if sales < 1000:
        bonus_amount = 0.1 * sales
    else:
        bonus_amount = 0.15 * sales
    print(f"Bonus: {bonus_amount:.0f}")


