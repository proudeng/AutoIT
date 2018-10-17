'''
Created on 2018/10/12

@author: edenjun
'''
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        return str(b2a_hex(self.ciphertext), encoding='utf-8')

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = str(cryptor.decrypt(a2b_hex(text)), encoding= 'utf-8')
        return plain_text.rstrip('\0')
