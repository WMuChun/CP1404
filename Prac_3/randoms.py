import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""
1. What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

--It randomly selects a number from 5 to 20 and displays it, and the smallest number is 5, and
the largest is 20.


2. What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

--It randomly select a number between (3, 5, 7, 9), and display it. Because the step is 2, so the line 2 can 
not produced a 4. the smallest number is 3, and the largest is 9


3. What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

--it returns a randomly floating point number, with value range of 2.5 <= N <= 5.5

"""

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

print(random.randint(1,100))