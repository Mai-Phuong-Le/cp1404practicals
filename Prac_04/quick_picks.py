import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
RANDOM_NUMBERS = 5

quick_pick_number = int(input("How many quick picks? "))
while quick_pick_number <= 0:
    print("Quick pick number is > 0")
    quick_pick_number =  int(input("How many quick picks? "))

for i in range(quick_pick_number):
    numbers = []
    for j in range(RANDOM_NUMBERS):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in numbers:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(number)

    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))