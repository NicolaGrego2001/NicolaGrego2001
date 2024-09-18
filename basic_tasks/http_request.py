import requests

# richieste dirette
print(requests.get('https://www.google.com'))



# ottengo testo
print(requests.get('https://www.google.com').text)

# ottengo status code
print(requests.get('https://www.google.com').status_code)


# sessione
session = requests.session()
response1 = session.get('https://www.google.com')
print(session.cookies)
response2 = session.get('https://www.google.com/search?client=firefox-b-d&q=ciao')
print(response2.cookies)
session.close()

# con context manager
with requests.Session() as s:
    r = s.get('https://www.google.com')
    print(r.status_code)
    print(s.cookies)

# qui la sessione viene chiusa automaticamente
