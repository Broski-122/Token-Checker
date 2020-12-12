import os
import requests as req
from colorama import Fore as COL, Style as ST

if os.path.exists('tokens.txt'):
    pass
else:
    open('tokens.txt', 'x', encoding='utf-8')
if os.path.exists('valid.txt'):
    pass
else:
    open('valid.txt', 'x', encoding='utf-8')
tokens = open('tokens.txt', 'r', encoding='utf-8').read().splitlines()

def check():
    print(COL.BLUE + f'Broski\'s Discord Token Checker Version 1.0\nPlease wait. . . . .\n')
    for authtoken in tokens:
        try:
            ss = req.get('http://discordapp.com/api/users/@me', headers={'authorization': authtoken})
        except req.exceptions.ConnectionError:
            pass
        if ss.status_code == 200:
            f = open('valid.txt', 'a')
            f.write(f'{authtoken}\n')
            f.close()
            print(COL.GREEN + f'{authtoken}')
        else:
            print(COL.RED + f'{authtoken}')
        if ss.status_code == 429:
            print(COL.RED + ST.BRIGHT + f'You are being rate limited. {ss.status_code}')
            exit()         
check()
