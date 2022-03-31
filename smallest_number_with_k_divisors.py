from factorize import factorize
from SieveOfEratosthenes import SieveOfEratosthenes
def smallest_number_with_k_divisors(k):
    primes, exponents = factorize(k)
    min = float('inf')
    