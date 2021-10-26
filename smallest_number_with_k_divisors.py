from factorize import factorize

def smallest_number_with_k_divisors(k):
    primes, exponents = factorize(k)
    min = float('inf')
    