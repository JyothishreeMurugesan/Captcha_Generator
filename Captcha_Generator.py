#Captcha Generator

from random import choice

A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvuxy0123456789"

captcha = " "
for i in range(5):
    captcha+=choice(A)

    print("Your captcha:",captcha)
