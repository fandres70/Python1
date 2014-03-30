#!/usr/bin/env python

# Returns the factorial of the argument "number"
def factorial(number):
    if number <= 1: #base case
        return 1
    else:
        return number*factorial(number-1)

#    product = 1
#    for i in range(number):
#        product = product * (i+1)
#    return product


user_input = int(raw_input("Enter a non-negative integer: "))

factorial_result = factorial(user_input)
print factorial_result
