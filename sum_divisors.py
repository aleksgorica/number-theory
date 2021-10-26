from factorize import factorize

def sum_divisors(n):
    primes, exponents = factorize(n)
    product = 1
    for i in range(len(primes)):
        prime = primes[i]
        expo = exponents[i]
        geometric = (prime ** (expo + 1) - 1) // (prime -1)
        print(prime, expo, geometric)
        product *= geometric
    return product