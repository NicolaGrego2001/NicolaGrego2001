from dataclasses import dataclass, asdict

@dataclass
class Utente:
    nome: str
    cognome: str
    username: str
    password: str
    email: str

    def __post_init__(self):
        if self.password == 'password':
            raise ValueError('La password è insicura')

try:
    utente1 = Utente(nome='Simone', cognome='Brazioli', username='s.brazioli', password='password', email='s.brazioli@next-data.com')
except ValueError as e:
    print(str(e))

#print(utente1)

details = {
    'nome': 'Simone',
    'cognome': 'Brazioli',
    'username': 's.brazioli',
    'password': 'vghkfcghk',
    'email': 's.brazioli@next-data.com'
}

utente2 = Utente(**details)

print(utente2)
print(asdict(utente2))
