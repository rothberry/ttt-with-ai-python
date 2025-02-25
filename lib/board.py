# init_board_mat = [["💯", "💯", "💯"],["💯", "💯", "💯"],["💯", "💯", "💯"]]
# test_board_mat = [["💯", "X", "💯"],["💯", "💯", "💯"],["💯", "O", "💯"]]

init_board = ["💯", "💯", "💯", "💯", "💯", "💯", "💯", "💯", "💯"]
test_board = ["💯", "X", "💯", "💯", "💯", "💯", "💯", "O", "💯"]


class Board:
    def __init__(self):
        self.board = test_board
        self.counter = 2
        # self.play_dict = {"X": [[0,1]], "O": [[2,1]]}
        self.play_dict = {"X": [2], "O": [8]}

    def display(self):
        print(f"===TURN={self.counter}===")
        i = 0
        while i < len(self.board):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            i += 3
            if i < 7:
                print("------------")
        print("============")

    def reset_board(self):
        self.board = init_board
        self.counter = 0

    @staticmethod
    def position(user_input):
        # takes in user input and converts to number
        # takes in string of number, we want that int minus 1
        # 1-9 or coords
        try:
            val = int(user_input) - 1
            if val in range(0,8):
              return val
            else:
              return False
        except ValueError:
            print("Not a vibe")

    def current_player(self):
        if self.counter % 2 == 0:
            return "O"
        else:
            return "X"

    def is_open(self, location):
        return self.board[location] == "💯"

    def place_marker(self, player, location):
        # update board and dict
        self.board[location] = player
        self.play_dict[player].append(location)
        self.counter += 1

    def turn(self):
        # check if board is full
        # take user input
        # run thro postion
        # check if that position is taken
        # use counter for current player
        # place marker

        user_in = input("Pick a Spot\n")
        user_pos = self.position(user_in)
        print(user_pos)
        if self.is_open(user_pos):
            self.place_marker(self.current_player(), user_pos)
        else:
            print("TAKEN")
        self.display()
        self.turn()


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
