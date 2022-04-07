init_board = [["💯", "💯", "💯"],["💯", "💯", "💯"],["💯", "💯", "💯"]]
test_board = [["💯", "X", "💯"],["💯", "💯", "💯"],["💯", "O", "💯"]]

class Board:
  
  def __init__(self):
    self.board = test_board
    self.counter = 0
    # Play turns
    # self.play_dict = {"X": [[0,1]], "O": [[2,1]]}
    self.play_dict = {"X": [2], "O": [8]}


  def display(self):
    print(f'===TURN={self.counter}===') # add in turn counter here too
    for index, row in enumerate(self.board):
      print(f"{row[0]} | {row[1]} | {row[2]}")
      if index != 2:
        print("---------")
    print("==========")

  @staticmethod
  def translate_coords(spot):
    # 2 => [0,1]
    # 7 => [2,0]
    # x = 7/3 - 1 => 2
    # x = 9/3 - 1 => 2

    # x = (spot/3) - 1
    # y = spot%3
    pass

  def reset_board(self):
    self.board = init_board
    self.counter = 0

  def position(self, user_input):
    # takes in user input and converts to number
    # takes in string of number, we want that int minus 1
    # 1-9 or coords
    try:
      return int(user_input) - 1
    except ValueError:
      return False

  def current_player(self):
    if self.counter % 2 == 0:
      return "O"
    else:
      return "X"


