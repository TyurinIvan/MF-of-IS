import numpy as np
from sympy import Matrix


def encode(text, alphabet):
    return [alphabet.index(c) for c in text]


def decode(data, alphabet):
    return "".join([alphabet[v] for v in data])


def get_inverse_key(key, M):
    return np.array(Matrix(*key.shape, key.reshape(-1)).inv_mod(M))


def encryptText(text, alphabet, key):
    M = len(alphabet)
    data = encode(text, alphabet)
    r = np.dot(np.array(data).reshape(-1, key.shape[0]), key.T) % M
    #print(r)
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
text = 'ARTISTICALLY'
abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

key = np.array([
    [1, 2, 2],
    [4, 5, 6],
    [7, 8, 9]
])

key = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

print(encryptText(text, abc, key))
print(decryptText(encryptText(text, abc, key),
                  abc, key))
