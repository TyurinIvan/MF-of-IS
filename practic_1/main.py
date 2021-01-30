class Affine(object):
    DIE = 128
    KEY1 = (7, 3, 55)
    KEY2 = (9, 22, 57)

    def __init__(self):
        pass

    def encryptChar(self, char, iter):
        return chr((iter[0] * ord(char) + iter[1]) % self.DIE)

    def encrypt(self, string):
        dirDictA, dirDictB, invDictA = Affine.calcMas(string)
        res = ''
        for i in range(len(string)):
            iter = [dirDictA[i], dirDictB[i], invDictA[i]]
            res += self.encryptChar(string[i], iter)
        return res

    def decryptChar(self, char, iter):
        return chr(iter[2] * (ord(char) - iter[1]) % self.DIE)

    def decrypt(self, string):
        dirDictA, dirDictB, invDictA = Affine.calcMas(string)
        res = ''
        for i in range(len(string)):
            iter = [dirDictA[i], dirDictB[i], invDictA[i]]
            res += self.decryptChar(string[i], iter)
        return res

    @classmethod
    def calcMas(cls, string):
        K1, K2, KI1 = cls.KEY1
        K3, K4, KI3 = cls.KEY2
        dirDictA = [K1, K3]
        dirDictB = [K2, K4]
        invDictA = [KI1, KI3]
        for i in range(2, len(string)):
            dirDictA.append(dirDictA[i - 1] * dirDictA[i - 2])
            dirDictB.append(dirDictB[i - 1] + dirDictB[i - 2])
            invDictA.append(invDictA[i - 1] * invDictA[i - 2])
        return dirDictA, dirDictB, invDictA


affine = Affine()

print(affine.encrypt('Affine Cipher'))
print(affine.decrypt('J,3>&Bq;H	'))

tmp = affine.encrypt('Affine Cipher')
tmpE = 'Affine Cipher'
cnt = 0
while tmp != tmpE:
    print(affine.encrypt(str(tmp)))
    tmp = affine.encrypt(tmp)
    cnt += 1
print(cnt)
