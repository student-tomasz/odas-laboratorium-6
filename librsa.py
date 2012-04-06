#!./env/bin/python

from Crypto.PublicKey import RSA
import modularmath, padstring

class LibRSA:
    KEYLENGTH = 2048

    def __init__(self, keylength = KEYLENGTH):
        self.key = RSA.generate(keylength)

    def encrypt(self, plain):
        padded = padstring.pad(plain)
        encrypted = []
        for chunk in padded:
            encrypted.append(modularmath.power(chunk, self.key.e, self.key.n))
        return encrypted

    def decrypt(self, encrypted):
        # decrypted = []
        # for chunk in encrypted:
        #     decrypted.append(modularmath.power(chunk, self.key.d, self.key.n))
        # return padstring.unpad(decrypted)
        decrypted = []
        for chunk in encrypted:
            decrypted.append(self.key.decrypt(chunk))
        return padstring.unpad(decrypted)



if __name__ == '__main__':
    librsa = LibRSA()
    plain = 'asdqwezxc'
    if plain == librsa.decrypt(librsa.encrypt(plain)):
        print 'passed'
    else:
        print 'failed'
