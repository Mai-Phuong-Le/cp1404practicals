"""What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
"""
# I see a random number from 5 to 20
# the smallest number was 6
# the largest number was 19

""" What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
"""
# I saw a random number from 3 to 10 with each number apart from each pother 2 units
# the smallest number was 3
# the largest number was 9
# No, it couldn't. Because it displayed a random number which started from 3 to 10 and apart from each pother 2 units

""" What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
"""
# I see a random number from 2.5 to 5.5
# the smallest number was 2.638323489913914
# the largest number was 4.753975263410754

""" Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
import random
print(random.randint(1,100))