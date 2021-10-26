from SieveOfEratosthenes import SieveOfEratosthenes

def factorize(n):
    possible_primes = SieveOfEratosthenes(n // 2)
    primes = []
    exponents = []
    index = 0    
    while n != 1:
        print(n, index, primes, exponents, possible_primes)
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

