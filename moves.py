from get_moves_data import get_move_data

class Move:
  def __init__(self, id):
    self.id, self.name, self.accuracy, self.pp, self.priority, self.power, self.type = get_move_data(id)
  
  def useMove(self):
    if self.pp == 0:
      return False
    else:
      self.pp -= 1
      return True