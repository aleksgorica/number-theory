from factorize import factorize
from SieveOfEratosthenes import SieveOfEratosthenes
import time


def sum_divisors(n, primes=None):
    primes, exponents = factorize(n, primes) if primes else factorize(n)
    product = 1
    for i in range(len(primes)):
        prime = primes[i]
        expo = exponents[i]
        geometric = (prime ** (expo + 1) - 1) // (prime - 1)
        product *= geometric
    return product


# print(sum_divisors(1))


def sumofamicables(n):
    sum = 0
    for i in range(1, n+1):
        a = sum_divisors(i)
        a = a - i
        if a <= 0:
            continue
        b = sum_divisors(a)
        b = b - a
        if i == b and a != b:
            print("match", i, a)
            sum += i
    return sum


def sumDivisors(n):
    count = 0
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            if i == n / i:
                count += i
            else:
                count += i + int(n / i)
    return count


def abundantSum(n):
    #primes = SieveOfEratosthenes(n)
    sum = 0
    abundants = []
    for i in range(1, n):
        if sumDivisors(i) > 2*i:
            abundants.append(i)
    nums = [True] * n
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            val1 = abundants[i]
            val2 = abundants[j]
            if val1 + val2 < n:
                nums[val1 + val2] = False
    for i in range(len(nums)):
        if nums[i]:
            sum += i
    print(sum)


    # print(sumofamicables(10000))
start = time.time()
print(start)
abundantSum(28124)
end = time.time()
print(end - start)
