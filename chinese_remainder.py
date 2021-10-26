from gcd import gcd

from modinv import modinv



def checkCoprime(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (i == j):
                continue
            if (gcd(nums[i], nums[j]) != 1):
                raise Exception(f"{nums[i]} and {nums[j]} arent coprime")
    return True

def chinese_remainder(remainders, moduli):
    if (len(remainders) != len(moduli)):
        raise Exception("length of remainders and moduli doesnt match")
    if (not checkCoprime(moduli)):
        raise Exception("Two numbers arent coprime")

    N = 1
    for a in moduli:
        N *= a

    Ni = [1] * len(moduli)
    for i in range(len(moduli)):
        Ni[i] = N // moduli[i]

    print("Ni")
    print(Ni)

    Ni_inverse = [0] * len(moduli)
    for i in range(len(Ni)):
        Ni_inverse[i] = modinv(Ni[i], moduli[i])
    print(Ni_inverse)
    solution = 0
    for i in range(len(Ni)):
        solution += Ni[i] * Ni_inverse[i] * remainders[i]

    print(f"N: {N}")

    return solution % N



    
    




