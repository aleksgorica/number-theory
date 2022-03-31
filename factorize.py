def SieveOfEratosthenes(n):
    if n == 0:
        return []
    sieve = [True] * (n+1)
    p = 2  # val = 2
    while (p * p <= n):
        if (sieve[p] == True):
            for i in range(p ** 2, n + 1, p):
                sieve[i] = False
        p += 1
    sieve[0] = False
    sieve[1] = False

    primes = []
    for i in range(len(sieve)):
        if sieve[i] == True:
            primes.append(i)

    return primes


# driver
if __name__ == "__main__":
    print("Sieve")
    print("0: ", SieveOfEratosthenes(0))
    print("1: ", SieveOfEratosthenes(1))
    print("2: ", SieveOfEratosthenes(2))
    print("30: ", SieveOfEratosthenes(30))


def factorize(n, primes=None):
    possible_primes = primes if primes else SieveOfEratosthenes(n // 2)
    primes = []
    exponents = []
    index = 0
    while n != 1 and index < len(possible_primes):
        if n % possible_primes[index] == 0:
            n = n // possible_primes[index]
            if possible_primes[index] in primes:
                exponents[len(primes) - 1] += 1
            else:
                primes.append(possible_primes[index])
                exponents.append(1)
        else:
            index += 1
    return (primes, exponents)
