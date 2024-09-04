with open('test', 'wt') as out_file:
    out_file.write('Pippo\n')

with open('test', 'rt') as in_file:
    testo_letto = in_file.read()
    print(testo_letto)

with open('test', 'wt') as out_file:
    out_file.write('Pluto\n')

with open('test', 'rt') as in_file:
    print(in_file.read())

with open('test', 'a') as out_file:
    out_file.write('Paperino\n')

with open('test', 'rt') as in_file:
    print(in_file.read())
