import json
import requests

class FileCache:
    def __init__(self, cache_file):
        self.cache_file = cache_file
        self.cache = self.load_cache()

    def load_cache(self):
        try:
            with open(self.cache_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_cache(self):
        with open(self.cache_file, "w") as file:
            json.dump(self.cache, file)

    def get(self, key, default=None):
        return self.cache.get(key, default)

    def set(self, key, value):
        self.cache[key] = value
        self.save_cache()

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            self.save_cache()

def fetch_pokemon_data(pokemon_id):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    try:
        response = requests.get(f"{base_url}{pokemon_id.lower()}")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None
