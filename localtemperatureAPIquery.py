import requests
import json
import owmcreds
import pprint

weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?'

payload_2 = {'q': 'CITY_NAME', 'units': 'metric', 'APPID': owmcreds.key}
response_city_name = requests.get(weather_api_url, params=payload_2)

i = json.loads(response_city_name.content)

# print(response_city_name.content)

print('The temperature in {} ({}) is currently {} degrees Celsius'.format(i['name'], i['sys']['country'], i['main']['temp']))

print('\n\nFull JSON output from API is: ')
pprint.pprint(f'{i}')

print(f'All information from {weather_api_url[:-1]}')

#payload = {'lat': 'xx.xx', 'lon': 'xx.xx', 'units': 'metric', 'APPID': owmcreds.key}

#response = requests.get(weather_api_url, params=payload)

# if response.status_code == 200:

#     print(response.content)
# else:
#     print('Error message {}'.format(response.status_code))
# i = json.loads(response.content)
