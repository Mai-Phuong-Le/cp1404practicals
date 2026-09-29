"""What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
"""
# I see display a random number between 5 to 20
# the smallest number is 6
# the largest number is 19
"""What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
"""
# I see a random number from 3 to 10 which apart from 2 units
# the smallest number was 3
# the largest number was 9
# No, it could not produce a 4 because the random range started at 3
# and each number apart from each other  units

""" What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
"""
# I saw a random number from 2.5 to 5.5
# the smallest number is 2.638323489913914
# the largest number is 4.753975263410754

"""
Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
import random
print(random.randint(1,100))