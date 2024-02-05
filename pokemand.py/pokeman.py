import requests 
url = 'https://pokeapi.co/api/v2/pokemon/21'
response = requests.get(url)

json_response = response.json()

print(json_response['abilities'][0]['ability']['name'])
print(json_response['forms'][0]['name'])