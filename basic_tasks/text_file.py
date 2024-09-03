with open('/tmp/test', 'wt') as out_file:
    out_file.write('Pippo\n')

with open('/tmp/test', 'rt') as in_file:
    print(in_file.read())

with open('/tmp/test', 'wt') as out_file:
    out_file.write('Pluto\n')

with open('/tmp/test', 'rt') as in_file:
    print(in_file.read())

with open('/tmp/test', 'a') as out_file:
    out_file.write('Paperino\n')

with open('/tmp/test', 'rt') as in_file:
    print(in_file.read())
