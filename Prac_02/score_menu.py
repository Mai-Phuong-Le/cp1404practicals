"""Menus"""
from Prac_01.broken_score import score
import random
MENU = "G(et), P(in), S(how), Q(uit)"

def main():
    score_user = get_valid_score()
    while True:
        print(MENU)
        choice_of_menu = input(">>> ")

def decide_choice(choice_of_menu):
    while choice_of_menu != "Q":
        if choice_of_menu == "G":
            return 0 <= score <= 100
        elif choice_of_menu == "P":
            get_score(score)
        elif choice_of_menu == "S":
            return "*" * score
        else:
            return "Finished"
    return None


def get_score(score_user):
    if score_user < 0 or score_user > 100:
        return "Invalid score"
    elif score_user >= 90:
        return "Excellent"
    elif score_user >= 50:
        return "Passable"
    else:
        return "Bad"

def get_valid_score():
    score_user = float(input("Enter score: "))
    while score_user < 0 or score_user > 100:
        print("Invalid score")
        score_user = float(input("Enter score: "))
    return score_user