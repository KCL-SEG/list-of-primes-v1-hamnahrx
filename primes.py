"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

#method to calculate prime numbers
# for i in range of count, calculate prime number and add to list

#function called is_prime
# takes single parameter 'num'
#
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    list = []
    #count = int(input("Enter an integer: "))
    count = 2

    while len(list) < number_of_primes:
        if is_prime(count):
            list.append(count)
        count += 1

    return list
