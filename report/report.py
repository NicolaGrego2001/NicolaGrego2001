"""
Script per creare il report
"""

# COSTANTI DI INPUT

IP_CENTRALINO = '192.168.1.101'
PORT = 8000
SSL = False
URI = "/calls.csv.gz"

IP_MARIADB = '192.168.1.101'
USERNAME_MARIADB = 'user'
PASSWORD_MARIADB = 'password'
DATABASE_MARIADB = 'gestionale'

CLIENTS_TABLE_MARIADB = 'clienti'
CLIENTS_ROW_KEYS = ['nome_azienda', 'numero_azienda']

OPERATORS_TABLE_MARIADB = 'operatori'
OPERATORS_ROW_KEYS = ['nome', 'numero_telefono']




