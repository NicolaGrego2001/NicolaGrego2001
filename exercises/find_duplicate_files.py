import glob
from pathlib import Path

elenco_file = glob.glob('./**', recursive=True)

set_file_visti = set()
# elemento -> ./es11.py  | ./dir2  | ./dir2/file_10
for elemento in elenco_file:
    if Path(elemento).is_file():
        filename = elemento.split('/')[-1]
        if filename in set_file_visti:
            print(f"{filename} già visto in precedenza")
        else:
            set_file_visti.add(filename)
    else:
        print(f"{elemento} is a directory!")
#filename = stringa.split('/')[-1]
#print(filename)
