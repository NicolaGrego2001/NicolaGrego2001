import requests

print(requests.get('https://www.google.com'))
print(requests.get('https://www.google.com').text)
response = requests.get('https://www.google.com')
print(response.text)

persistent_connection = requests.session()
response = persistent_connection.get('https://www.google.com')
print(persistent_connection.cookies)
response = persistent_connection.get('https://www.google.com/search?client=firefox-b-d&q=ciao')
print(response.text)
