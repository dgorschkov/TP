# https://static-maps.yandex.ru/1.x/?ll=37.677751,55.757718&spn=0.016457,0.00619&l=map
# http://geocode-maps.yandex.ru/1.x/?apikey=&geocode=Ульяновск&format=json

import requests

host = 'https://static-maps.yandex.ru/1.x/'
params_query = {
    'll': '37.677751,55.757718',
    'spn': '0.016457,0.00619',
    'l': 'map',
}

resp = requests.get(host, params=params_query)
print(resp.status_code)
# print(resp.text)
print(resp.reason)
print(resp.url)
with open('map.png', mode='wb') as f:
    f.write(resp.content)
