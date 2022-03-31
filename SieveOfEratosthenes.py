def SieveOfEratosthenes(n):
    if n == 0: return []
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

#driver
if __name__ == "__main__":
    print("0: ", SieveOfEratosthenes(0))
    print("1: ", SieveOfEratosthenes(1))
    print("2: ", SieveOfEratosthenes(2))
    print("30: ", SieveOfEratosthenes(30))


