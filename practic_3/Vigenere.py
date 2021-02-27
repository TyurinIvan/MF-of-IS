def encryptText(text, key, abc):
    return ''.join([abc[(abc.index(j) + abc.index(key[i])) % 26 + abc.index('A')] for i, j in enumerate(text)])


def decrtptText(decodedText, key, abc):
    return ''.join([abc[(abc.index(j) - abc.index(key[i])) % 26 + abc.index('A')] for i, j in enumerate(decodedText)])


def createKey(key, text, myType, abc):
    l = len(text)
    k = len(key)

    if myType == 'repeat':
        res = (key * int((l // k + 1)))[:l]
    elif myType == 'open':
        res = key[0] + text[:-1]
    elif myType == 'cipher':
        key = key[:1]
        for j, i in enumerate(text[:-1]):
            c = abc[(abc.index(i) + abc.index(key[j])) % len(abc)]
            key += c
        res = key

    return res


abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text = 'ARTISTICALLY'
key = 'ABC'
myType = 'repeat'  # repeat | open | cipher


k = createKey(key, text, myType, abc)
print('Key:           ', k)

encryptedText = encryptText(text, k, abc)
print('Encrypted text:', encryptedText)
print('Decrypted text:', decrtptText(encryptedText, k, abc))
