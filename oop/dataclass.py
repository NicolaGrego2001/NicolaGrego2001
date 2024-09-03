class Utente:
    def __init__(self, nome, cognome, username, password, email):
        self.nome = nome
        self.cognome = cognome
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}, Username: {self.username}, Email: {self.email}"

    def __eq__(self, other):
        return self.username == other.username and self.password == other.password and self.email == other.email

# creo utente con dati random
utente1 = Utente("John", "Doe", "jsmith", "secretpassword", "john.doe@example.com")

# creo altro utente con stessi dati
utente2 = Utente("John", "Doe", "jsmith", "secretpassword", "john.doe@example.com")

print(utente1 == utente2)

print(utente1.email)
utente1.password = 'altrapassword'
print(utente1)

import dataclasses

@dataclasses.dataclass
class Utente_dc:
    nome: str
    cognome: str
    username: str
    password: str
    email: str

# creo utente con stessi dati
utente1 = Utente_dc("John", "Doe", "jsmith", "secretpassword", "john.doe@example.com")
utente2 = Utente_dc("John", "Doe", "jsmith", "secretpassword", "john.doe@example.com")


print(utente1 == utente2)

print(utente1.email)
utente1.password = 'altrapassword'
print(utente1)

# modifica email utente2
utente2.email = 'new.john.doe@example.com'

print(utente2.email)
print(utente2)


