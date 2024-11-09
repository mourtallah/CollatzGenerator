"""
Collatz Sequence Generator

This script generates the Collatz sequence for a given number.
The Collatz sequence is defined as follows:
- Start with any positive integer n.
- Then each term is obtained from the previous term as follows:
  - If the previous term is even, the next term is one half of the previous term.
  - If the previous term is odd, the next term is 3 times the previous term plus 1.
The sequence ends when it reaches the number 1.

Author: Mourtallah Faye
Date: 2023-04-30
"""
import random
import matplotlib.pyplot as plt

# User input
while True:
    try:
        user_input = int(input("Enter a number: "))
        starting_number = user_input
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Initialize sequence and stopping time
collatz_sequence = []
stopping_time = 1

# Generate sequence
while starting_number != 1:
    collatz_sequence.append(int(starting_number))
    if starting_number % 2 == 0:
        starting_number = starting_number/2
    else:
        starting_number = 3*starting_number + 1
    stopping_time += 1

# Print results
if len(collatz_sequence) > 20:
    print("A sample of 20 elements from the Collatz Sequence for the number " +
          str(user_input) + " is:")
    print([int(collatz_sequence[i]) for i in sorted(random.sample(range(len(collatz_sequence)), 20))], end="")
    print(",")
else:
    print("The Collatz Sequence for the number " + str(user_input) + " is:")
    print(collatz_sequence, end="")
    print(",")
print("This sequence has a total stopping time of " + str(stopping_time) + ".")
if user_input == 1:
    print("The number 1 has no Collatz Sequence, so the peak of the sequence is 1.")
else:
    print("The peak of the sequence is " + str(max(collatz_sequence)) + ".")
plt.plot(collatz_sequence)
plt.show()

