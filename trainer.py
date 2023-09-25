from pokemon import Pokemon

class Trainer:
  def __init__(self, name, pokemon):
    self.name = name
    self.pokemon = []
    for poke in pokemon:
      self.pokemon.append(Pokemon(poke))

  def capturePokemon(self, name):
    self.pokemon.append(Pokemon(name))

  def releasePokemon(self, name):
    for i in range(len(self.pokemon)):
      if self.pokemon[i].name == name:
        self.pokemon.pop(i)
        break
  
  def printPokemon(self):
    print('Pokemon: ', end='')
    for pokemon in self.pokemon:
      print(pokemon.name.capitalize(), end=' ')
    print('')


if __name__ == '__main__':
  Ayman = Trainer('Ayman', ['charmander', 'ditto', 'bulbasaur'])
  Ayman.printPokemon()

  Ayman.capturePokemon('pikachu')
  Ayman.printPokemon()

  Ayman.releasePokemon('charmander')
  Ayman.printPokemon()
