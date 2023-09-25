import requests
from fileCache import FileCache

def get_pokemon_data(pokemon_id):
    pokemon_id = str(pokemon_id)
    cache = FileCache("pokemon_cache.json")
    cached_data = cache.get(pokemon_id)


    if cached_data is None:
        # Data not found in cache, fetch from the PokeAPI
        pokemon_data = fetch_pokemon_data(pokemon_id)

        if pokemon_data:
            # Store the fetched data in the cache
            cache.set(pokemon_id, pokemon_data)
            cached_data = pokemon_data

    return extract_data(cached_data)


def fetch_pokemon_data(pokemon_id):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon_id = str(pokemon_id)
    try:
        response = requests.get(f"{base_url}{pokemon_id.lower()}")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None


def extract_data(data):

    # Extract relevant information from the JSON response
    id = data['id']
    name = data['name']
    base_experience = data['base_experience']
    height = data['height']
    weight = data['weight']
    abilities = [a['ability']['name'] for a in data['abilities']]
    forms = data['forms']
    sprites = data['sprites']

    stat_names = [s['stat']['name'] for s in data['stats']]
    stats_stats = [s['base_stat'] for s in data['stats']]
    stats = {k: v for k, v in zip(stat_names, stats_stats)}

    moves = [m['move']['name'] for m in data['moves']]
    types = [t['type']['name'] for t in data['types']]

    # # Print the Pokemon's data
    # print(f"ID: {id}")
    # print(f"Name: {name.capitalize()}")
    # print(f"Types: {', '.join(types)}")
    # print(f"Abilities: {', '.join(abilities)}")
    # print(f"Moves: {', '.join(moves[0:4])}")

    return id,name,base_experience,height,weight,abilities,forms,sprites,stats,moves,types



if __name__ == "__main__":
    # Prompt the user to enter a Pokemon name
    print(get_pokemon_data('charmander')[10])
