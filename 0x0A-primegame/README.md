
Prime Game
This Python module defines a function isWinner that determines the winner of a game based on prime numbers. The game involves two players, Maria and Ben, taking turns removing numbers from a given set.

Installation
There's no special installation required for this module. It's a standalone Python script that can be used by importing it into your Python project.

Usage
python
Copy code
from prime_game import isWinner

# Define the numbers set
numbers = [10, 15, 20]

# Determine the winner
winner = isWinner(2, numbers)
print(winner)  # Output: Winner: Ben
Functionality
isWinner(x, nums)
This function takes two arguments:

x: An integer representing the initial value.
nums: A list of integers representing the numbers to be considered in the game.
It iterates through each number in the list nums, playing a game where players alternate turns. On each turn, the player must remove a prime number and all its multiples from the current set of numbers. If a player cannot make a move (no prime numbers left), their opponent wins.

The function returns a string indicating the winner of the game ("Winner: Maria" or "Winner: Ben"), or None if it's a tie.

is_prime(n)
This helper function checks if a given number n is a prime number. It returns True if n is prime, and False otherwise.

primes_in_range(start, end)
This helper function returns a list of prime numbers within the specified range [start, end], inclusive.

Example
Consider the following example:

python
Copy code
numbers = [10, 15, 20]
winner = isWinner(2, numbers)
print(winner)  # Output: Winner: Ben
In this example, Maria and Ben play with the numbers [10, 15, 20], and Maria starts first (as indicated by x=2). After playing the game according to the rules described above, the function determines that Ben is the winner.

License
This module is released under the MIT License. Feel free to use and modify it according to your needs.
