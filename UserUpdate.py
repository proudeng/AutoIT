'''
Created on 2018/10/12

@author: edenjun
'''
import os
import json
import getpass
from mycrypt import prpcrypt

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
    user_dict = { eid:{"email":email,"passwd":epasswd_enc}}
    
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
