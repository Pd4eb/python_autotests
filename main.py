import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1e5405868450408e5d1a9d137b3340b8'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}


body_create ={
    "name": "Бульбазавр",
    "photo_id": 1
}
pokemon={
    "pokemon_id": "308336"
}

edit={
    "pokemon_id": "308335",
    "name": "Pd4eb",
    "photo_id": 2
}
'''response = requests.post(url= f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''


'''response_confirmation = requests.post(url=f'{URL}/trainers/confirm_email', headers=HEADER,json=body_confirmation)
print(response_confirmation.text)'''


response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER,json=body_create)
print(response_create.text)

response_create = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER,json=pokemon)
print(response_create.text)

response_create = requests.put(url=f'{URL}/pokemons', headers=HEADER,json=edit)
print(response_create.text)