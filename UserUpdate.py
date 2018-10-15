'''
Created on 2018/10/12

@author: edenjun
'''
import os
import getpass
import json
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
#        return self.ciphertext

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
#        plain_text = cryptor.decrypt(text)
        return plain_text.rstrip('\0')

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self.obj)



if __name__ == '__main__':
    print("This tool works for the Auto Time-Reporting system.You can use it to add yourself into the system and you can use it to update your password.");
    pc = prpcrypt("proudengxiaoshee")
    AddOrModify = ""
    while AddOrModify not in ["A","M"]:
        AddOrModify = input("Please choose to add new user or modify the existing user( input 'A' or 'M'):")
        
    eid = input("Please input your eid:")
    email = input("Please input your Ericsson mail address:")
    epasswd = getpass.getpass("Please input your Ericsson Password:")
    epasswd_enc = pc.encrypt(epasswd)
    user_dict = { eid:[email,epasswd_enc]}
    
    if os.path.exists("user.json"):
        fb = open("user.json",'r')
        data = json.load(fb)
        data[eid] = user_dict[eid]
        fb.close()
    else:
        data = user_dict

    fp = open("user.json",'w+')
    json.dump(data,fp)
    fp.close()
