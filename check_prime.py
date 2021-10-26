from SieveOfEratosthenes import SieveOfEratosthenes

def check_prime(n):
    primes = SieveOfEratosthenes(n//2)
    for prime in primes:
        if n % prime == 0:
            return False
    return True