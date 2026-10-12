"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
from typing import Any


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        # string concatenation
        # income = float(input("Enter income for month " + str(number_of_months) + ": "))
        incomes.append(income)


    calculate_income(incomes, number_of_months)



def calculate_income(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print_report(income, month, total)



def print_report(income, month, total):
    "Display report"
    # format method
    print( "Month {:2} - Income: ${:8.2f} Total: ${:10.2f}".format(month, income, total))
    # print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()