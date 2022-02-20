#BİSMİLLAHİRRAHMANİRRAHİM 

import random
import string
import os
import colorama
from colorama import Fore, Back, Style


def clear():
    os.system('cls')
#Renkler
blue = '\033[1;34;48m'
green = '\033[1;32;48m'
red = '\033[1;31;48m'
yellow ='\033[1;33;48m'
abc ='\033[1;37;48m'
abcc ='\033[1;36;48m'

colorama.init(autoreset=True)

symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []

print ()
print (f'''
{green}| {blue}Günveli Şifre @ardatuna {green}\----------------------------\n
'''  )


length = input(f'{green}> {blue}Password uzunluğu : {abcc} ')
length = int(length)

while count < length:
    rand = random.randint (0,3)
    if rand == 0:
        lower += 1
        b = int(random.randint (97,123))
        password.append(b)
    elif rand == 1:
        upper += 1
        b = random.randint (65,91)
        password.append(b)
    elif rand == 2:
        number += 1
        b = random.randint (48,58)
        password.append(b)
    elif rand == 3:
        r = random.randint(0,2)
        symbol += 1
        if r == 0:
            b = random.randint (33,48)
            password.append(b)
        elif r == 1:
            b = random.randint (91,97)
            password.append(b)
        elif r == 2:
            b = random.randint (123,126)
            password.append(b)
    count += 1
password = "".join([chr(c) for c in password])

print (f"{blue}>{green} Password : {abc}" + password)