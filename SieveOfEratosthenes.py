def SieveOfEratosthenes(n):
    sieve = [True] * (n+1)
    p = 2 #val = 2
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


