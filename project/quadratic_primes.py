from check_prime import check_prime

for i in range(100):
    print(i, i**2 + i + 41, check_prime(i**2 + i + 41))
