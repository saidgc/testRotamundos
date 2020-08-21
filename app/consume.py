import requests as r
import json
from collections import namedtuple

def getAllPokemons():
    reponse = r.get('https://pokeapi.co/api/v2/pokemon/?limit=100')
    pokemons = []
    index = 1
    for pokemon in json.loads(reponse.text)['results']:
        pokemons.append((index, pokemon))
        index += 1
    return pokemons

def getPokemon(id):
    response = r.get('https://pokeapi.co/api/v2/pokemon/'+ str(id) +'/')
    details = json.loads(response.text)
    return details

def getAllPokemonsByType(type):
    pokemonByType = []
    pokemons = getAllPokemons()
    id_pokemon = 1
    for pokemon in pokemons:
        pokemon_details = getPokemon(id_pokemon)
        for types in pokemon_details['types']:
            if types['type']['name'] == type:
                pokemonByType.append(pokemon)
                break
        id_pokemon += 1
    
    return pokemonByType


getAllPokemonsByType('grass')
# getPokemon(1)