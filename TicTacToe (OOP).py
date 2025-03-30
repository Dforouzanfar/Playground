import numpy as np
import random


class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), '')

    def __line_checker__(self, line):
        line = ''.join(line)
        if len(line) == 3:
            if len(set(line)) == 1:
                print('Player %s wins!' % set(line).pop())
                return True

    def __board_checker__(self):
        game_ends = False

        for i in range(3):
            if self.__line_checker__(self.board[i]):
                game_ends = True
                break

            if self.__line_checker__(self.board.T[i]):
                game_ends = True
                break

        else:
            if self.__line_checker__(np.diag(self.board)):
                game_ends = True
            elif self.__line_checker__(np.diag(np.fliplr(self.board))):
                game_ends = True

        return game_ends

    def __moves_checker__(self):
        empty_spots = np.where(self.board == '')
        allowed_moves = []

        for i in range(len(empty_spots[0])):
            row = empty_spots[0][i]
            column = empty_spots[1][i]

            allowed_moves.append((row, column))

        return allowed_moves

    def play(self):
        print(self.board, '\n')

        while True:
            allowed_moves = self.__moves_checker__()

            row, column = random.choice(allowed_moves)
            self.board[row][column] = 'o'
            print(self.board, '\n')

            if self.__board_checker__():
                break

            allowed_moves = self.__moves_checker__()

            while True:
                row, column = input().split()
                if (int(row), int(column)) in allowed_moves:
                    self.board[int(row)][int(column)] = 'x'
                    break
                else:
                    print('Invalid move.')
            print(self.board, '\n')

            if self.__board_checker__():
                break

        self.__init__()

game = TicTacToe()
game.play()