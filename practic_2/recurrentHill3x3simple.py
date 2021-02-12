import numpy as np
from numpy.linalg import det, inv

modinvDebug = False
encryptTextDebug = False
decryptTextDebug = False
createDecryptKeyDebug = False
mainPartDebug = False


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    if modinvDebug:
        print('a, m:', a, m)
    g, x, y = egcd(a, m)
    if modinvDebug:
        print('g, x, y:', g, x, y)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def encode(text, alphabet):
    return [alphabet.index(c) for c in text]


def decode(data, alphabet):
    return "".join([alphabet[v] for v in data])


def get_inverse_key(key, M):
    d = round(det(key)) % M
    return np.array(np.round(inv(key) * d) * round(modinv(d, M)), dtype=int) % M


def encryptText(text, alphabet, key1, key2):
    text = checkText(text)
    M = len(alphabet)
    N = (len(text) // key1.shape[0]) + 1
    if encryptTextDebug:
        print('M, N:', M, N)
    key = createKey(key1, key2, N, alphabet)
    data = encode(text, alphabet)
    if encryptTextDebug:
        print('data:', data)

    cnt = 0
    res = np.zeros(shape=(N - 1, 3), dtype='int_')
    for i in np.array(data).reshape(-1, key.shape[1]):
        if encryptTextDebug:
            print(i)
        res[cnt] = np.dot(i, key[cnt].T) % M
        cnt += 1

    if encryptTextDebug:
        print('res', res)
    pt = decode(res.flatten(), alphabet)
    return pt


def decryptText(text, alphabet, key1, key2, ):
    M = len(alphabet)
    N = (len(text) // key1.shape[0]) + 1
    if decryptTextDebug:
        print('N:', N)
    key = createDecryptKey(key1, key2, N, alphabet)
    if decryptTextDebug:
        print('Key:', key)
    data = encode(text, alphabet)

    cnt = 0
    res = np.zeros(shape=(N - 1, 3), dtype='int_')
    for i in np.array(data).reshape(-1, key.shape[1]):
        res[cnt] = np.dot(i, key[cnt].T) % M
        if decryptTextDebug:
            print(key[cnt])
        cnt += 1
    if decryptTextDebug:
        print(data)
        print(res)
    pt = decode(res.flatten(), alphabet)
    return pt


def createKey(key1, key2, sizeStop, alphabet):
    M = len(alphabet)
    keyDim = key1.shape[0] if (key1.shape[0] == key1.shape[1] and
                               key2.shape[0] == key2.shape[1]) else 0
    if keyDim == 0:
        raise ValueError("Матрицы ключей должны быть квадратными")

    key = np.concatenate((key1, key2), axis=0)

    for _ in range(sizeStop - 2):
        mult = np.dot(key2, key1) % M
        key1 = np.copy(key2)
        key2 = np.copy(mult)
        key = np.concatenate((key, mult), axis=0)

    key.shape = (-1, keyDim, keyDim)
    return key


def createDecryptKey(key1, key2, sizeStop,
                     alphabet='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
    if createDecryptKeyDebug:
        print('SizeStop:', sizeStop)
    M = len(alphabet)
    keyDim = key1.shape[0] if (key1.shape[0] == key1.shape[1] and
                               key2.shape[0] == key2.shape[1]) else 0
    if keyDim == 0:
        raise ValueError("Матрицы ключей должны быть квадратными")

    key1inv = get_inverse_key(key1, M)
    key2inv = get_inverse_key(key2, M)
    keyInv = np.concatenate((key1inv, key2inv), axis=0)
    if createDecryptKeyDebug:
        print('KeyInv: ', keyInv)

    for _i in range(sizeStop - 2):
        if createDecryptKeyDebug:
            print('key1do:', _i, key1)
            print('key2do:', _i, key2)
            print('key1doInv:', _i, key1inv)
            print('key2doInv:', _i, key2inv)
            print(get_inverse_key(key1, M))
        multInv = np.dot(key1inv, key2inv) % M
        mult = np.dot(key2, key1) % M
        if createDecryptKeyDebug:
            print('multInv:', _i, multInv)
            print('mult:', _i, mult)
        key1inv = np.copy(key2inv)
        key2inv = np.copy(multInv)
        key1 = np.copy(key2)
        key2 = np.copy(mult)

        if createDecryptKeyDebug:
            print('key1:', _i, key1)
            print('key2:', _i, key2)

        keyInv = np.concatenate((keyInv, multInv), axis=0)

    keyInv.shape = (-1, keyDim, keyDim)
    if createDecryptKeyDebug:
        print(keyInv)
    return keyInv


def checkText(text):
    if len(text) % 3 == 0:
        return text
    elif len(text) % 3 == 1:
        return text + 'AA'
    else:
        return text + 'A'


# text = 'ГНГНЪДЛНВПЬМЕЩЪ'
# text = 'ГНГНЪДЖХКЕТЖРЮТ'
text = 'CRYPTOGRAPHY'
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

key1 = np.array([
    [1, 2, 0],
    [0, 1, 4],
    [1, 2, 2]
])

key2 = np.array([
    [1, 2, 0],
    [0, 1, 4],
    [1, 2, 2]
])

key3 = np.array([
    [1, 2, 2],
    [4, 5, 6],
    [7, 8, 9]
])

key4 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [2, 2, 1]
])

key5 = np.array([
    [1, 1],
    [3, 4]
])

key6 = np.array([
    [4, 3],
    [1, 1]
])

key7 = np.array([
    [16, 3],
    [21, 17]
])

keyTest = np.array([
    [12, 10, 25],
    [2, 17, 0],
    [17, 22, 25]
])

key1inv = np.array([
    [25, 2, 25],
    [18, 7, 2],
    [18, 8, 25]
])

key2inv = np.array([
    [1, 16, 25],
    [6, 15, 20],
    [19, 4, 6]
])

if mainPartDebug:
    print(np.dot(key1inv, key2inv) % 26)
    print(get_inverse_key(key6, 26))
    print(get_inverse_key(keyTest, 26))

print(encryptText(text, abc, key3, key4))
print(decryptText(encryptText(text, abc, key3, key4),
                  abc, key3, key4))
if mainPartDebug:
    print(decryptText('MYIIWTYQBNUXRGE',
                      abc, key3, key4))
