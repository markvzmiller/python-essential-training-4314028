# def allPrimesUpTo(num):

# def allPrimesUpTo(num):

def allPrimesUpTo(num):
    listOfPrimes = []
    for number in range(0, num):
        for factor in range(2, int(number ** 0.5) + 1):
            if number % factor == 0:
                break # any time factor not found breaks loop
        else:
            listOfPrimes.append(number)  

    return listOfPrimes

# teacher solution--an efficient way to to check for primes
#
# def allPrimesUpTo(num):
#     primes = [2]
#     for number in range(3, num):
#         sqrtNum = number**0.5
#         for factor in primes:
#             if number % factor == 0: # if true, not prime, we break and move on
#                 # Not prime
#                 break
#             if factor > sqrtNum: # if the number is greater than square root it is a prime number
#                 # It's prime!
#                 primes.append(number)  # append to list
#                 break
#     return primes

