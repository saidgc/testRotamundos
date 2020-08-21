from app import app, consume
from flask import render_template, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', pokemons=consume.getAllPokemons())

@app.route('/pokemon/<pokemon_id>')
def viewPokemon(pokemon_id):
    pokemons = consume.getAllPokemons()
    name = pokemons[int(pokemon_id) - 1 ][1]['name']
    return render_template(
        'pokemon.html', 
        pokemon=consume.getPokemon(pokemon_id), 
        id=pokemon_id,
        name=name
        )


@app.route('/tipo/<type>')
def viewPokemonByType(type):
    return render_template('bytype.html', type=type, pokemons=consume.getAllPokemonsByType(type))
