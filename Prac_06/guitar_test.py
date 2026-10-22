from guitar import Guitar
import datetime

current_year = datetime.datetime.now().year

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 1000)

print(f"{guitar.name} get_age() - Expected {current_year - 1922}. Got {guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected {current_year - 2013}. Got {another_guitar.get_age()}")

print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
