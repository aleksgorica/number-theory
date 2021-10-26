from egcd import egcd


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('inverse doesnt exist')
    else:
        return x % m