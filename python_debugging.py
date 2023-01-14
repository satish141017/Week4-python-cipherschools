import pdb 
# modeule : python files contain useful classes or function that is written by developers
# our first module
# debugging:
# ya hamare code ke run hone mai error aye ya code sahi chal raha hai but output sahi nahi aa raha code mai galtiyoon ko dhoond ke sahi karne ko debugging khete hai
name=input("Name : ")
pdb.set_trace()
age=input("age : ")
print(name,age+1)


# # commands=>
# 1. l    to shhow were code is stopped
# 2. c    to run code without debugging
# 3. q    to quit from run
# 4. n    to go to next line
