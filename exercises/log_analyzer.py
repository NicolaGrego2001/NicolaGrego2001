# scrivere script per analizzare un file e mandare mail alla prima riga
# che contiene una stringa specificata

# SUGGERIMENTO:
# per cercare una sottostringa all'interno di una stringa più grande, possiamo utilizzare
# la keyword 'in'

# 'pippo' in 'pluto e pippo' -> True
# 'pippo' in 'topolino e archimede' -> False
# 'pippo' in 'pippoide' -> True
# 'pippo' in 'agamennone' -> False

# ->
# if 'pippo' in 'pippoide':
#    print('Sì')
# else:
#    print('No')
import re
def send_mail(s: str) -> None:
    import smtplib
    from email.mime.text import MIMEText

    with open('/tmp/password.txt', 'rt') as in_password:
        password = in_password.read().splitlines()[0]
    username = 's.brazioli@next-data.com'

    with smtplib.SMTP_SSL('smtp.next-cloud.it', 465) as smtp_server:
        smtp_server.login(username, password)

        msg = MIMEText(s)
        msg['Subject'] = "ALERT! Tentativo di accesso"
        msg['From'] = 's.brazioli@next-data.com'
        msg['To'] = 'administrator@brazioli.com'

        smtp_server.send_message(msg)
        print("Email sent successfully.")

# Capire quali stringhe dobbiamo cercare -> "Invalid user"
string_to_find = 'Invalid user'
# Aprire il file
with open('../auth.log', 'rt') as in_log:
    tutto_il_file = in_log.read()
    righe = tutto_il_file.splitlines()
# controllare se string_to_find è presente all'interno
print(f"Lunghezza log {len(righe)}")
elenco_righe = []
for riga in righe:
    print(riga)
    if string_to_find in riga:
        print(f"Sì")
        elenco_righe.append(riga.split(sep=' ')[-3])
        """con regex
        x = re.match(pattern=r'.* (\d+\.\d+\.\d+\.\d+) .*', string=riga)
        print(x)
        ip = x[1]
        elenco_righe.append(ip)
        """
        # qui mando mail
        # send_mail(riga)
    else:
        print(f"No")

print(elenco_righe)
elenco_righe = set(elenco_righe)
print(len(elenco_righe))
elenco_righe_str = '\n'.join(elenco_righe)
send_mail(elenco_righe_str)
"""
if string_to_find in elemento0:
    print("Sì")
    exit(0)
elemento1 = righe[1]
if string_to_find in elemento1:
    print("Sì")
    exit(0)
elemento2 = righe[2]
"""
# per ogni riga dovremo controllare se è presente la stringa ricercata

# se è vero mandiamo la mail e interrompiamo

# altrimenti prossima riga

