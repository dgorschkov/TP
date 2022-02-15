import requests

host = 'http://geocode-maps.yandex.ru/1.x/'
params_query = {
    'apikey': '',
    'geocode': 'Самара',
    'format': 'json',
}

resp = requests.get(host, params=params_query)
print(resp.status_code)
print(resp.json())
print(resp.reason)
print(resp.url)
with open('data.json', mode='w', encoding='utf8') as f:
    f.write(resp.text)
resp = resp.json()
data = resp["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
print(data["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"])
