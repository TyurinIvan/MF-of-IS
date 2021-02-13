import numpy as np
from numpy.linalg import det, inv

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def get_inverse_matrix(key, M):
    d = round(det(key)) % M
    return np.array(np.round(inv(key) * d) * round(modinv(d, M)), dtype=int) % M
