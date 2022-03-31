from SieveOfEratosthenes import SieveOfEratosthenes


def check_prime(n):
    primes = SieveOfEratosthenes(n//2)
    for prime in primes:
        if n % prime == 0:
            return False
    return True


if __name__ == "__main__":
    print(7, check_prime(7))
    print(10, check_prime(10))
