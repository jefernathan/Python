# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
    print('\033[;31mO site pudim.com.br não esta acessível no momento\033[m')
else:
    print('\033[;32mO site pudim.com.br esta acessível no momento\033[m')
