from get_pokemon_data import get_pokemon_data
from type_text_slowly import type_text_slowly
import random
from moves import Move

class Pokemon:
  def __init__(self, id):
    self.id, self.name, self.base_experience, self.height, self.weight, self.abilities, self.forms, self.sprites, self.stats, self.moves, self.types = get_pokemon_data(id)
    self.maxHP = self.stats['hp']
    self.setMoves()

  def setMoves(self):
    move_names = []
    moves = []

    if len(self.moves) > 4:
       num = 4
    else:
       num = len(self.moves)

    while len(move_names) < num:
      randomMove = random.choice(self.moves)
      if randomMove not in move_names:
        move_names.append(randomMove)

    for move in move_names:
       moves.append(Move(move))
    
    self.moves = moves

  def getHealth(self):
    return self.stats['hp']
  
  def setHealth(self, health):
    self.stats['hp'] = health

  def take_damage(self, damage):
      self.stats['hp'] -= damage
      if self.stats['hp'] < 0:
          self.stats['hp'] = 0

  def is_fainted(self):
      return self.stats['hp'] <= 0
  
  def printHealth(self):
     healthBar = '=' * int(10 // (self.maxHP /self.stats['hp']))
     print(healthBar)
     print(f"{self.name.capitalize()}'s HP: {round(self.stats['hp'],1)}")
     
  def printMoves(self):
     print(f"Which move should {self.name.capitalize()} use?")
     print('')
     for i in range(len(self.moves)):
        print(f"{i+1}. {self.moves[i].name.capitalize()}")
        print(f"PP: {self.moves[i].pp}")
        print('')

  def useMove(self, move):
     moveIndex = [move.name.lower() for move in self.moves].index(move)

     if self.moves[moveIndex].useMove():
        print('')
        type_text_slowly(f"{self.name.capitalize()} used {move.capitalize()}!")
        print('')
        return True
     else:
        type_text_slowly(f"You can't use that move anymore!")
        return False

if __name__ == '__main__':
  Pikachu = Pokemon('pikachu')
  Pikachu.take_damage(10)
  print(Pikachu.moves)
