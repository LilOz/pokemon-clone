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

  def takeDamage(self, damage):
      self.stats['hp'] -= damage
      if self.stats['hp'] < 0:
          self.stats['hp'] = 0

  def isFainted(self):
      return self.stats['hp'] <= 0
  
  def printHealth(self):
     healthBar = '=' * int(20 // (self.maxHP / self.stats['hp']))
     print(f"{self.name.capitalize()}'s HP: {round(self.stats['hp'],1)}")
     print(healthBar)
     
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
        type_text_slowly(f"{self.name.capitalize()} can't use that move anymore!")
        return False
     
  def alterStats(self, move, isOpponentMove):
   if isOpponentMove:
      for statChange in move.stat_changes:
         if statChange['change'] < 0:
            self.stats[statChange['stat']['name']] += statChange['change']
            type_text_slowly(f"{self.name.capitalize()}'s {statChange['stat']['name']} was decreased!")
   else:
      for statChange in move.stat_changes:
         if statChange['change'] > 0:
            self.stats[statChange['stat']['name']] += statChange['change']
            type_text_slowly(f"{self.name.capitalize()}'s {statChange['stat']['name']} was increased!")


if __name__ == '__main__':
  Pikachu = Pokemon('pikachu')
  Pikachu.take_damage(10)
  print(Pikachu.stats)
