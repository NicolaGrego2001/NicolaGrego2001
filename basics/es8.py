# dict

# def
my_dict = {
    'nome': 'Simone',
    'cognome': 'Brazioli',
    'eta': 29
}

print(my_dict)

# get value from key
print(my_dict['nome'])
print(my_dict.get('cognome'))

# iter methods
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

for key, value in my_dict.items():
    print(f'Chiave: {key}, Valore: {value}')

# mutable
print(id(my_dict))
my_dict.pop('nome')
print(id(my_dict))

# extend
altro_dict = {
    'citta': 'Imola',
    'provincia': 'Bologna'
}
my_dict.update(altro_dict)
print(my_dict)

# shallow copy(*)
copy_dict = my_dict.copy()
print(id(my_dict))
print(id(copy_dict))

# clear
print(my_dict.clear())
print(my_dict)
print(id(my_dict))

# mutable <-> copy
passioni = ['computer', 'astronomia']
diz1 = {
    'nome': 'Simone',
    'cognome': 'Brazioli',
    'passioni': passioni
}

print(diz1)
# diz2 = diz1.copy()

import copy

diz2 = copy.deepcopy(diz1)
print(diz2['nome'])
diz2['nome'] = 'Gianluca'
diz2['eta'] = 25
diz2['nuovo'] = 'pippo'
print(f"Stampo il valore: {diz2['nuovo']}")
diz2['passioni'].append('corsa')

print(diz1)
print(diz2)