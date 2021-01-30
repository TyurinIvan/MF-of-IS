alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']

alphabet1 = ['e', 'd', 'n', 'q', 'v', 'm', 'r', 'z', 'b', 'h', 'g', 'a', 'f', 'w', 'k', 'l', 'x', 'c', 't', 's', 'o',
            'j', 'p', 'i', 'u', 'y']

''' Функция шифрования по ключу
    text - list символов текста
    key - list с перестановкой на алфавите'''


def encrypt(__text__, __key__):
    result = ''
    for i in range(len(__text__)):
        result += (__key__[alphabet.index(__text__[i])])

    return result


# Press the green button in the gutter to run the script.
if __name__ == 'replacement':
    text = 'my text'
    key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']
    ciphertext = encrypt(text, key)
    print(ciphertext)
    ciphertext = encrypt(ciphertext, key)
    print(ciphertext)
