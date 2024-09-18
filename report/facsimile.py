"""
Obiettivo: fornire al reparto commerciale un report delle chiamate fatte dai colleghi operatori
#################################
### DATI IN INPUT ###

# Centralino (RESTAPI)
IP_CENTRALINO: str = 'XXX.XXX.XXX.XXX'
SSL: bool = False
URI: str = /calls.csv.gz

# MariaDB (mysql.connector)
IP_MARIADB: str = 'XXX.XXX.XXX.XXX'
USERNAME_MARIADB: str = 'username'
PASSWORD_MARIADB: str = 'password'
DATABASE_MARIADB: str = 'gestionale'
CLIENTS_TABLE_MARIADB: str = 'clienti'
CLIENTS_ROW_KEYS = ['nome_azienda', 'numero_azienda']

OPERATORS_TABLE_MARIADB: str = 'operatori'
OPERATORS_ROW_KEYS = ['nome', 'numero_telefono']

#################################

Lo script deve fornire in stdout:
    - il numero di chiamate e i secondi effettuati verso ciascun cliente
    - il numero di chiamate e i secondi effettuati da ciascun operatore
    - per ogni operatore, il cliente verso cui ha trascorso il maggior tempo al telefono

#################################

Schema mentale:

- scarica il file calls.csv.gz
- decomprimere (lato OS o dentro Python?)
- caricare file decompresso
- aprire il file csv
- caricare i dati in un formato comodo per poter essere cercato
- analizzare i dati dal db per sostituire al numero di telefono il nome di ciascun azienda
- analizzare i dati dal db per sostituire al numero di telefono il nome di ciascun operatore
- aggregare i dati
- stampare
"""
