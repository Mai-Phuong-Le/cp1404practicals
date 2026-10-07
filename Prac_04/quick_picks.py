import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        numbers = []

        while len(numbers) < NUMBERS_PER_PICK:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)

            if number not in numbers:
                numbers.append(number)

        numbers.sort()

        for number in numbers:
            print(f"{number:2}", end=" ")
        print()


main()