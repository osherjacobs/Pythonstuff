import requests
import json
import owmcreds
import pprint
import time
import pyfiglet

heading = pyfiglet.figlet_format("OJ's Gratuitous Weather App")
print(heading)
weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?'

payload_2 = {'q': 'CITY_NAME', 'units': 'metric', 'APPID': owmcreds.key}
response_city_name = requests.get(weather_api_url, params=payload_2)

i = json.loads(response_city_name.content)

print('The temperature in {} ({}) is currently {} degrees Celsius'.format(i['name'], i['sys']['country'], i['main']['temp']))

sunset = i['sys']['sunset']
sundown = time.localtime(sunset)
print('Sunset is at {:2d}:{:2d}:{:02d} today ({}/{}/{})'.format(sundown.tm_hour, sundown.tm_min, sundown.tm_sec, sundown.tm_mday, sundown.tm_mon, sundown.tm_year))
print('\n')
print(f'Full JSON output of API from {weather_api_url[:-1]}: ')

pprint.pprint(i)
