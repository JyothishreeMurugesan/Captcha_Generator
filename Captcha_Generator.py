#Captcha Generator

from random import choice

A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a="abcdefghijklmnopqrstuvuxyz"
Num = "0123456789"

captcha = " "
for i in range(5):
    captcha+=choice(A)+choice(a)+choice(Num)

    print("Your captcha:",captcha)
