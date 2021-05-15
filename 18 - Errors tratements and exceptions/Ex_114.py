import requests

try:
    requests.get('http://pudim.com.br/')
except:
    print('Não consegui')
else:
    print('Consegui!')
