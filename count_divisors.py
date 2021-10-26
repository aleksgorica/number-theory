from factorize import factorize

def count_divisors(n):
    primes, exponents = factorize(n)
    count = 1
    for i in exponents:
        count *= (i + 1)
    return count
