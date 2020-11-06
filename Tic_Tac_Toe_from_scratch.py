#Objective: Coding Tic Tac Toe from scratch

import random


class Board:
    def __init__(self):
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.available_spots = set()
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                self.available_spots.add((i, j))

    def print_board(self):
        for line in self.board:
            print(line)

    def is_full(self):
        return all(self.board[0]) and all(self.board[1]) and all(self.board[2])


class Agent():
    def __init__(self):
        self.position = [None,None]
        self.marker = 'O'
        self.name = 'computer'
        self.count_coords = {'row0': 0, 'row1': 0, 'row2': 0,
                'col0': 0, 'col1': 0, 'col2': 0, 'diag1': 0, "diag2": 0}

    def ask_user(self):
        inp = input('input the coordinates in format r,c you want to play (row and column between 1-3) ')
        row = int(inp.split(',')[0])-1
        column = int(inp.split(',')[1])-1
        return row, column

    def is_winner(self):
        return any(value == 3 for value in self.count_coords.values())


class HumanAgent:
    def __init__(self):
        self.marker = 'X'
        self.name = 'You'
        self.count_coords = {'row0': 0, 'row1': 0, 'row2': 0,
                'col0': 0, 'col1': 0, 'col2': 0, 'diag1': 0, "diag2": 0}

    def is_winner(self):
        return any(value == 3 for value in self.count_coords.values())


class TicTacToe(Board, Agent, HumanAgent):
    def __init__(self):
        Board.__init__(self)
        HumanAgent.__init__(self)
        Agent.__init__(self)
        self.HumanAgent = HumanAgent()
        self.Agent = Agent()
        self.active_agent = None

    def mark_board(self, row, column, marker):
        self.board[row][column] = marker

    def make_move(self):
        if self.active_agent == self.HumanAgent:
            row,column = self.ask_user()
            while row < 0 or row > 2 or column < 0 or column > 2 or self.board[row][column]:
                print("taken spot or invalid range, try another another coordinate")
                row, column = self.ask_user()
        else:
            (row,column) = random.sample(self.available_spots,1)[0]
            # row = row_col[0]
            # column = row_col[1]

        self.available_spots.discard((row,column))
        # Mark the board
        self.mark_board(row, column, self.active_agent.marker)
        self.active_agent.count_coords['row'+str(row)] += 1
        self.active_agent.count_coords['col' + str(column)] += 1
        if row == column:
            self.active_agent.count_coords['diag1'] += 1
        if (row,column) in [(0,2), (1,1), (2,1)]:
            self.active_agent.count_coords['diag2'] += 1

    def play_game(self):
        while not self.is_full():
            # initialize
            print('\n')
            if not self.active_agent:
                self.active_agent = self.HumanAgent
            # if existing agent from the last round change the agent
            elif self.active_agent == self.HumanAgent:
                self.active_agent = self.Agent
            elif self.active_agent == self.Agent:
                self.active_agent = self.HumanAgent

            self.make_move()
            self.print_board()

            if self.active_agent.is_winner():
                print(" Game finished! The winner is ", self.active_agent.marker)
                if not self.another_round():
                    return
        print("Board is full game finished")
        self.another_round()
        return

    def another_round(self):
        play_again = input(" Would you like to play one more round? yes/no: ")
        if play_again=='yes':
            self.__init__()
            self.play_game()
        else:
            print("goodbye!")
            return False


if __name__ == "__main__":
        game = TicTacToe()
        game.print_board()
        game.play_game()



