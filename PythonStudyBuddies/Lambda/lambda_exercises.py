# Create a lambda function that takes one parameter (a) and returns it.
lambda a : a

# Summarize argument a, b, and c and return the result
# To return the result with the python interpreter use >>>_(1, 2, 3)
x = lambda a, b, c : a + b + c
print(x(1, 2, 3))

# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument
x = lambda a : a + 15 
print(x(8))

# Write a function definition that takes one argument n, and that argument will be multiplied with an unknown number a
def func(n):
    return lambda a : a * n
    
print(func(2)(5)) 

# Notes:
#   Choose wisely between lambdas or normal Python functions
#   Avoid excessive use of lambdas
#   Use lambdas with higher-order functions or Python key functions
