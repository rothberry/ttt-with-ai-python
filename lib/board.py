# TODO: WRITE AN EXIT
# init_board_mat = [["💯", "💯", "💯"],["💯", "💯", "💯"],["💯", "💯", "💯"]]
# test_board_mat = [["💯", "X", "💯"],["💯", "💯", "💯"],["💯", "O", "💯"]]
import os

init_board = ["💯", "💯", "💯", "💯", "💯", "💯", "💯", "💯", "💯"]
test_board = ["💯", "X", "💯", "💯", "💯", "💯", "💯", "O", "💯"]
test_board_x = ["X", "X", "X", "O", "💯", "💯", "O", "O", "💯"]

WINNING_COMBO = [[0,1,2],[3,4,5],[6,7,8],[0,3,6], [1,4,7],[2,5,8],[0,4,8],[2,4,6]]
class Board:
    def __init__(self):
        # TODO creat board from dict
        self.board = init_board.copy()
        self.counter = 0
        # TODO make init counter & play_dict dynamic
        # self.play_dict = {"X": [[0,1]], "O": [[2,1]]}
        # self.play_dict = {"X": [1], "O": [7]}
        self.play_dict = {"X": [], "O": []}

    def display(self):
        
        os.system('clear')
        print(f"===TURN=`{self.current_player()}`===")
        i = 0
        while i < len(self.board):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            i += 3
            if i < 7:
                print("------------")
        print("============")


    def reset_board(self):
        self.board = init_board.copy()
        self.counter = 0

    @staticmethod
    def position(user_input):
        # takes in user input and converts to number
        # takes in string of number, we want that int minus 1
        # 1-9 or coords
        try:
            val = int(user_input) - 1
            if val in range(0,9):
              return val
            else:
              return False
        except ValueError:
            print("Not a vibe")

    def current_player(self):
        if self.counter % 2 == 0:
            return "X"
        else:
            return "O"

    def is_open(self, location):
        return self.board[location] == "💯"

    def place_marker(self, player, location):
        # update board and dict
        self.board[location] = player
        self.play_dict[player].append(location)
      
    def handle_input(self, user_input): 
        ui = user_input.lower()
        if(ui == "reset"):
            self.reset_board()
            self.display()
            self.turn()
            return True
        if(ui == "exit"):
            return True


    def turn(self):
        # check if board is full
        # take user input
        # run thro postion
        # check if that position is taken
        # use counter for current player
        # place marker
        
        user_in = input("Pick a Spot\n")
        if(self.handle_input(user_in)):
            return
        user_pos = self.position(user_in)

        print(user_pos)
        if self.is_open(user_pos):
            self.place_marker(self.current_player(), user_pos)
        else:
            print("TAKEN")
        self.display()
        if(self.is_game_over()):
            return
        self.counter += 1
        self.turn()
        

    def is_game_over(self):
        # check if x or o has winning combo
        # check if board is full
        print(f"{self.play_dict}")
        if self.is_winner(self.current_player()):
            print("WINNER IS " + self.current_player())
            return True
        elif self.is_draw():
            print("GAME DRAW")
            return True
        return False

    def is_winner(self, player):
        # if player_dict[player].has_winning combo
        # return True, else return False
        if len(self.play_dict[player]) < 3:
            return False

        has_won = True
      
        for combo in WINNING_COMBO:
            # for c in combo:
            # loop over combo,
            # for each iteration, does self.player_dict[player] include c
            for c in combo:
                if not c in self.play_dict[player]:
                    has_won = False
                    break
                # has_won = True
            if has_won:
                break
        return has_won

    def is_draw(self):
        return self.counter > 8

    # For board matrix
    @staticmethod
    def translate_coords(spot):
        # 2 => [0,1]
        # 7 => [2,0]
        # x = 7/3 - 1 => 2
        # x = 9/3 - 1 => 2

        # x = (spot/3) - 1
        # y = spot%3
        pass

    def display_matrix(self):
        print(f"===TURN={self.counter}===")  # add in turn counter here too
        for index, row in enumerate(self.board):
            print(f"{row[0]} | {row[1]} | {row[2]}")
            if index != 2:
                print("---------")
        print("==========")
