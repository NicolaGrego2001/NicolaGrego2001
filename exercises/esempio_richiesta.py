import requests


r = requests.get('https://www.next-data.com')

print(r.cookies)
#print(r.text)
