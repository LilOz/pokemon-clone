from pokemon import Pokemon
from trainer import Trainer
from type_text_slowly import type_text_slowly
import random
import os
import art

TYPE_MODS = {
    "Normal": {
        "Normal": 1.0, "Fire": 1.0, "Water": 1.0, "Electric": 1.0, "Grass": 1.0,
        "Ice": 1.0, "Fighting": 1.0, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0,
        "Psychic": 1.0, "Bug": 1.0, "Rock": 0.5, "Ghost": 0.0, "Steel": 0.5, "Dragon": 1.0,
        "Dark": 1.0, "Fairy": 1.0
    },
    "Fire": {
        "Normal": 1.0, "Fire": 0.5, "Water": 0.5, "Electric": 1.0, "Grass": 2.0,
        "Ice": 2.0, "Fighting": 1.0, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0,
        "Psychic": 1.0, "Bug": 2.0, "Rock": 0.5, "Ghost": 1.0, "Steel": 2.0, "Dragon": 0.5,
        "Dark": 1.0, "Fairy": 1.0
    },
    "Water": {
        "Normal": 1.0, "Fire": 2.0, "Water": 0.5, "Electric": 1.0, "Grass": 0.5,
        "Ice": 1.0, "Fighting": 1.0, "Poison": 1.0, "Ground": 2.0, "Flying": 1.0,
        "Psychic": 1.0, "Bug": 1.0, "Rock": 2.0, "Ghost": 1.0, "Steel": 1.0, "Dragon": 0.5,
        "Dark": 1.0, "Fairy": 1.0
    },
    "Electric": {
        "Normal": 1.0, "Fire": 1.0, "Water": 2.0, "Electric": 0.5, "Grass": 0.5,
        "Ice": 1.0, "Fighting": 1.0, "Poison": 1.0, "Ground": 0.0, "Flying": 2.0,
        "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Steel": 1.0, "Dragon": 0.5,
        "Dark": 1.0, "Fairy": 1.0
    },
    "Grass": {
        "Normal": 1.0, "Fire": 0.5, "Water": 2.0, "Electric": 1.0, "Grass": 0.5,
        "Ice": 1.0, "Fighting": 1.0, "Poison": 0.5, "Ground": 2.0, "Flying": 0.5,
        "Psychic": 1.0, "Bug": 2.0, "Rock": 1.0, "Ghost": 1.0, "Steel": 0.5, "Dragon": 0.5,
        "Dark": 1.0, "Fairy": 1.0
    },
    "Ice": {
        "Normal": 1.0, "Fire": 0.5, "Water": 0.5, "Electric": 1.0, "Grass": 2.0,
        "Ice": 0.5, "Fighting": 2.0, "Poison": 1.0, "Ground": 2.0, "Flying": 2.0,
        "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Steel": 0.5, "Dragon": 2.0,
        "Dark": 1.0, "Fairy": 1.0
    },
    "Fighting": {
        "Normal": 2.0, "Fire": 1.0, "Water": 1.0, "Electric": 1.0, "Grass": 1.0,
        "Ice": 1.0, "Fighting": 1.0, "Poison": 0.5, "Ground": 1.0, "Flying": 0.5,
        "Psychic": 0.5, "Bug": 0.5, "Rock": 2.0, "Ghost": 0.0, "Steel": 2.0, "Dragon": 1.0,
        "Dark": 2.0, "Fairy": 0.5
    },
    "Poison": {
        "Normal": 1.0, "Fire": 1.0, "Water": 1.0, "Electric": 1.0, "Grass": 2.0,
        "Ice": 1.0, "Fighting": 1.0, "Poison": 0.5, "Ground": 0.5, "Flying": 1.0,
        "Psychic": 2.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 0.5, "Steel": 0.0, "Dragon": 1.0,
        "Dark": 1.0, "Fairy": 2.0
    },
    "Ground": {
        "Normal": 1.0, "Fire": 2.0, "Water": 1.0, "Electric": 2.0, "Grass": 0.5,
        "Ice": 1.0, "Fighting": 1.0, "Poison": 2.0, "Ground": 1.0, "Flying": 0.0,
        "Psychic": 1.0, "Bug": 0.5, "Rock": 2.0, "Ghost": 1.0, "Steel": 2.0, "Dragon": 1.0,
        "Dark": 1.0, "Fairy": 1.0
    },
    "Flying": {
        "Normal": 1.0, "Fire": 1.0, "Water": 1.0, "Electric": 2.0, "Grass": 0.5,
        "Ice": 2.0, "Fighting": 0.5, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0,
        "Psychic": 1.0, "Bug": 2.0, "Rock": 0.5, "Ghost": 1.0, "Steel": 0.5, "Dragon": 1.0,
        "Dark": 1.0, "Fairy": 1.0
    },
    "Psychic": {
        "Normal": 1.0, "Fire": 1.0, "Water": 1.0, "Electric": 1.0, "Grass": 1.0,
        "Ice": 1.0, "Fighting": 2.0, "Poison": 2.0, "Ground": 1.0, "Flying": 1.0,
        "Psychic": 0.5, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Steel": 0.5, "Dragon": 1.0,
        "Dark": 0.0, "Fairy": 1.0
    },
    "Bug": {
        "Normal": 1.0, "Fire": 0.5, "Water": 1.0, "Electric": 1.0, "Grass": 2.0,
        "Ice": 1.0, "Fighting": 0.5, "Poison": 0.5, "Ground": 1.0, "Flying": 0.5,
        "Psychic": 2.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 0.5, "Steel": 0.5, "Dragon": 1.0,
        "Dark": 2.0, "Fairy": 0.5
    },
    "Rock": {
        "Normal": 1.0, "Fire": 2.0, "Water": 1.0, "Electric": 1.0, "Grass": 1.0,
        "Ice": 2.0, "Fighting": 0.5, "Poison": 1.0, "Ground": 0.5, "Flying": 2.0,
        "Psychic": 1.0, "Bug": 2.0, "Rock": 1.0, "Ghost": 1.0, "Steel": 0.5, "Dragon": 1.0,
        "Dark": 1.0, "Fairy": 1.0
    },
    "Ghost": {
        "Normal": 0.0, "Fire": 1.0, "Water": 1.0, "Electric": 1.0, "Grass": 1.0,
        "Ice": 1.0, "Fighting": 0.0, "Poison": 0.5, "Ground": 1.0, "Flying": 1.0,
        "Psychic": 2.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 2.0, "Steel": 1.0, "Dragon": 1.0,
        "Dark": 2.0, "Fairy": 1.0
    },
    "Steel": {
        "Normal": 1.0, "Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Grass": 1.0,
        "Ice": 2.0, "Fighting": 2.0, "Poison": 0.0, "Ground": 2.0, "Flying": 0.5,
        "Psychic": 1.0, "Bug": 1.0, "Rock": 2.0, "Ghost": 1.0, "Steel": 0.5, "Dragon": 1.0,
        "Dark": 1.0, "Fairy": 2.0
    },
    "Dragon": {
        "Normal": 1.0, "Fire": 1.0, "Water": 1.0, "Electric": 1.0, "Grass": 1.0,
        "Ice": 1.0, "Fighting": 1.0, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0,
        "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Steel": 0.5, "Dragon": 2.0,
        "Dark": 1.0, "Fairy": 0.0
    },
    "Dark": {
        "Normal": 1.0, "Fire": 1.0, "Water": 1.0, "Electric": 1.0, "Grass": 1.0,
        "Ice": 1.0, "Fighting": 0.5, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0,
        "Psychic": 2.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 0.5, "Steel": 1.0, "Dragon": 1.0,
        "Dark": 0.5, "Fairy": 0.5
    },
    "Fairy": {
        "Normal": 1.0, "Fire": 0.5, "Water": 1.0, "Electric": 1.0, "Grass": 1.0,
        "Ice": 1.0, "Fighting": 2.0, "Poison": 0.5, "Ground": 1.0, "Flying": 1.0,
        "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Steel": 0.5, "Dragon": 2.0,
        "Dark": 2.0, "Fairy": 1.0
    }
}



class Battle:
  def __init__(self, trainer1, trainer2):
    self.trainer1 = trainer1 # User
    self.trainer2 = trainer2 # AI
    self.selectPokemon()

  def caclulateDamage(self, attack, defense, power, typeAttacking, typeDefending, typeMove):
    if attack is None or defense is None or power is None:
      return 0
    if typeMove == typeAttacking:
      stab = 1.2
    else:
      stab = 1

    mod = TYPE_MODS[typeAttacking][typeDefending] * stab
    damage = 0.5 * power * (attack/defense) * mod

    return damage/10

  def selectPokemon(self):
    valid = False
    while not valid:
      type_text_slowly(f"{self.trainer1.name} choose your pokemon!")
      self.trainer1.printPokemon()
      print('')
      self.trainer1_choice = input()
      if self.trainer1_choice.lower() in [poke.name.lower() for poke in self.trainer1.pokemon]:
        valid = True
        type_text_slowly(f"Go {self.trainer1_choice.capitalize()}!")
        print('')
        self.trainer2_choice = random.choice([poke.name.lower() for poke in self.trainer2.pokemon])
        type_text_slowly(f"{self.trainer2.name} chooses {self.trainer2_choice.capitalize()}!")
        print('')
      else:
        type_text_slowly(f"You can only choose a Pokemon that you have!")
        print('')
    self.battle()
  
  def battle(self):
    index_trainer1_pokemon = [poke.name.lower() for poke in self.trainer1.pokemon].index(self.trainer1_choice.lower())
    index_trainer2_pokemon = [poke.name.lower() for poke in self.trainer2.pokemon].index(self.trainer2_choice.lower())

    type_text_slowly(f"{self.trainer1.name} with {self.trainer1_choice.capitalize()} vs {self.trainer2.name} with {self.trainer2_choice.capitalize()}!")
    while (not self.trainer1.pokemon[index_trainer1_pokemon].is_fainted()) and (not self.trainer2.pokemon[index_trainer2_pokemon].is_fainted()):
      print('')
      print('')
      self.trainer1.pokemon[index_trainer1_pokemon].printHealth()
      print('')
      self.trainer2.pokemon[index_trainer1_pokemon].printHealth()
      print('')
      self.trainer1.pokemon[index_trainer1_pokemon].printMoves()

      valid = False
      while not valid:
        selection = input()
        if selection in ['1','2','3','4']:
          if self.trainer1.pokemon[index_trainer1_pokemon].useMove(self.trainer1.pokemon[index_trainer1_pokemon].moves[int(selection)-1].name):
            valid = True
        else:
          type_text_slowly("Invalid choice, try again:")
          print('')
          self.trainer1.pokemon[index_trainer1_pokemon].printMoves()

      trainer1Move = self.trainer1.pokemon[index_trainer1_pokemon].moves[int(selection)-1]

      valid = False
      while not valid:
        trainer2Move = random.choice(self.trainer2.pokemon[index_trainer2_pokemon].moves)
        if self.trainer2.pokemon[index_trainer2_pokemon].useMove(trainer2Move.name):
          valid = True
          trainer2Move = random.choice(self.trainer2.pokemon[index_trainer2_pokemon].moves)

      damageToPokemon2 = self.caclulateDamage(self.trainer1.pokemon[index_trainer1_pokemon].stats['attack'], self.trainer2.pokemon[index_trainer2_pokemon].stats['defense'], trainer1Move.power, self.trainer1.pokemon[index_trainer1_pokemon].types[0].capitalize(), self.trainer2.pokemon[index_trainer2_pokemon].types[0].capitalize(), trainer1Move.type['name'])
      damageToPokemon1 = self.caclulateDamage(self.trainer2.pokemon[index_trainer2_pokemon].stats['attack'], self.trainer1.pokemon[index_trainer1_pokemon].stats['defense'], trainer2Move.power, self.trainer2.pokemon[index_trainer2_pokemon].types[0].capitalize(), self.trainer1.pokemon[index_trainer1_pokemon].types[0].capitalize(), trainer2Move.type['name'])

      self.trainer2.pokemon[index_trainer2_pokemon].take_damage(damageToPokemon2)
      if(self.trainer2.pokemon[index_trainer2_pokemon].is_fainted()):
        print('')
        type_text_slowly(f"{self.trainer2.pokemon[index_trainer2_pokemon].name.capitalize()} has fainted!")
        type_text_slowly(f"{self.trainer1.name} wins!")
        print('')

      self.trainer1.pokemon[index_trainer1_pokemon].take_damage(damageToPokemon1)
      if(self.trainer1.pokemon[index_trainer1_pokemon].is_fainted()):
        print('')
        type_text_slowly(f"{self.trainer1.pokemon[index_trainer1_pokemon].name.capitalize()} has fainted!")
        type_text_slowly(f"{self.trainer2.name} wins!")
        print('')


      



if __name__ == '__main__':
  os.system('clear')
  type_text_slowly(art.text2art('Pokemon'), 0.001)

  Ayman = Trainer('Ayman', ['Charmander', 'Pikachu', 'Mewtwo'])
  Laura = Trainer('Laura', ['Squirtle', 'Charizard', 'Ditto'])

  battle = Battle(Ayman, Laura)
  input()