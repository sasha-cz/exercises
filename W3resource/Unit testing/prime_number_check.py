# Exercise_1: Write a Python unit test program to check if a given number is prime or not.

# list_of_prime_numbers_until_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Import the unittest module for unit testing
import unittest

# Define a function to check if a number is prime or not.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# Create testcases for the function is_prime(number).
# Create a class that inherits from unittest.TestCase
class TestPrimeNumberCheck(unittest.TestCase):
    # Create a method to test if the prime_number_check function recognizes prime numbers.
    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        print(f"Prime numbers: {prime_numbers}")
        for number in prime_numbers:
            self.assertTrue(is_prime(number)), f"Test fail: {number} is not recognized as a prime number."
    # Create a method to test if a number is wrongly recognized as a prime number.
    def test_non_prime_numbers(self):
        non_prime_numbers = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 
                             21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 
                             35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 
                             50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 
                             65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 
                             81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 
                             95, 96, 98, 99, 100]
        print(f"Non-prime numbers: {non_prime_numbers}")
        for number in non_prime_numbers:
            self.assertFalse(is_prime(number)), f"Test fail: {number} is wrongly recognized as a prime number"

if __name__ == '__main__':
    # Run the test cases
    unittest.main()

    