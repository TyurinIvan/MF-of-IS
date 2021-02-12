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


def encode(text, alphabet):
    return [alphabet.index(c) for c in text]


def decode(data, alphabet):
    return "".join([alphabet[v] for v in data])


def get_inverse_key(key, M):
    d = round(det(key))
    return np.array(np.round(inv(key) * d) * round(modinv(d, M)), dtype=int) % M


def encryptText(text, alphabet, key):
    M = len(alphabet)
    data = encode(text, alphabet)
    r = np.dot(np.array(data).reshape(-1, key.shape[0]), key.T) % M
    print(r)
    pt = decode(r.flatten(), alphabet)
    return pt


def decryptText(text, alphabet, key):
    M = len(alphabet)
    data = encode(text, alphabet)
    keyinv = get_inverse_key(key, M)
    r = np.dot(np.array(data).reshape(-1, key.shape[0]), keyinv.T) % M
    pt = decode(r.flatten(), alphabet)
    return pt


# text = 'ГНГНЪДЛНВПЬМЕЩЪ'
text = 'ЗНАТНЫЙБЫЛВОЗОК'
abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = np.array([
    [1, 2, 0],
    [0, 1, 4],
    [1, 2, 2]
])

print(encryptText(text, abc, key))
print(decryptText(encryptText(text, abc, key),
                  abc, key))
