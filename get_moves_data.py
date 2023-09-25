import requests
from fileCache import FileCache

def get_move_data(move_id):
    cache = FileCache("moves_cache.json")
    cached_data = cache.get(move_id)


    if cached_data is None:
        # Data not found in cache, fetch from the PokeAPI
        move_data = fetch_pokemon_data(move_id)

        if move_data:
            # Store the fetched data in the cache
            cache.set(move_id, move_data)
            cached_data = move_data
    return extract_data(cached_data)


def fetch_pokemon_data(move_id):
    base_url = "https://pokeapi.co/api/v2/move/"
    try:
        response = requests.get(f"{base_url}{move_id.lower()}")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None


def extract_data(data):

    # Extract relevant information from the JSON response
    id = data['id']
    name = data['name']
    accuracy = data['accuracy']
    pp = data['pp']
    priority = data['priority']
    power = data['power']
    type = data['type']

    return id, name, accuracy, pp, priority, power, type




if __name__ == "__main__":
    # Prompt the user to enter a Pokemon name
    print(get_move_data('bide'))