import os

import requests

url = 'https://sample-videos.com/csv/Sample-Spreadsheet-500000-rows.csv'
file_path = './test.csv'

def with_requests():

    response = requests.get(url)

    # salva il file
    if response.status_code == 200:
        # se la richiesta è andata a buon fine, salvo il file
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'File salvato con successo in {file_path}')
    else:
        print(f'Impossibile salvare il file. Status code: {response.status_code}')

def with_os_system():
    """
    Solo su linux, da controllare come su windows
    :return:
    """
    os.system(f'wget {url} -O {file_path}')


with_requests()
#with_os_system()