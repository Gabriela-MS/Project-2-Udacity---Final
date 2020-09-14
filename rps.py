# Writen and interpreted at PyCharm CE - Finally a decent interpreter!!!.
# Writen following Python 3 changes/novelties.
import random
from time import sleep
from unidecode import unidecode
# coding: utf-8
"""FINAL FILE!!!"""
"""This program plays a game of Rock, Paper, Scissors between two Players, """
"""and reports both Player's scores each round."""

""" In doubt check: https://docs.python.org/2.7/tutorial/ """

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players in this game."""


class Player:
    my_move = 0
    pc_move = 0

    def learn(self, my_move, pc_move):
        self.my_move = my_move
        self.pc_move = pc_move


def move():
    while True:
        human_choice = input('Please choose: rock, paper, or scissors:')
        if human_choice.lower() not in moves:
            print('\n !!! ERROR: choice not valid !!!\n')
            sleep(1.8)
        else:
            break
    return human_choice.lower()


class HumanPlayer(Player):
    # noinspection PyMethodMayBeStatic
    def move(self):
        return move()


""" A Player that always plays 'rock' """


class RockPlayer(Player):
    # noinspection PyMethodMayBeStatic
    def move(self):
        return moves[0]


""" chooses its move at random.  """


class RandomPlayer(Player):
    # noinspection PyMethodMayBeStatic
    def move(self):
        return random.choice(moves)


""" remembers what move the opponent played last round, and plays that move this round.  """


class ReflectPlayer(Player):
    def move(self):
        if self.pc_move == 'paper':
            return 'paper'
        elif self.pc_move == 'scissors':
            return 'scissors'
        else:
            return 'rock'


""" remembers what move it played last round, and cycles through the different moves.
(If it played 'rock' this round, it should play 'paper' in the next round.) """


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


""" Attention from line 107 -  Use of 'f-strings' check: 
https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/ """
""" Range - line 135: check https://pynative.com/python-range-function/#for-i-in-range-8211-for-loop-with-range"""


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played: {move1} and the computer: {move2} \n")
        sleep(1.0)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print(f"In a match between {move1} and {move2}, {move1} WINS! \n")
            sleep(0.7)
            print("* * * * * * You won! * * * * * *\n")
            sleep(1.8)
            self.p1_score += 1
        elif beats(move2, move1):
            print(f"In a match between {move2} and {move1}, {move2} WINS!\n")
            sleep(0.7)
            print("* * * * * * The computer won! * * * * * *\n")
            sleep(1.8)
            self.p2_score += 1
        else:
            print("* * * * * * Oh-oh! It's a tie! * * * * * *\n")
            sleep(1.8)

    def play_game(self):
        print("* * * * * * Welcome to the ROCK, PAPER, SCISSORS game. * * * * * *\n")
        print("Here are the rules: \n")
        print("Rock vs Paper -> Paper wins \n"
              "Rock vs Scissor -> Rock wins \n"
              "Paper vs Scissor -> Scissor wins \n")
        sleep(2.8)
        while True:
            for round in range(10):
                print(f"ROUND NUMBER: {round + 1}     |     SCORE: You: {self.p1_score} Computer: {self.p2_score}")
                self.play_round()
                if (round == 9) and self.p1_score < self.p2_score:
                    print(f"* * * * * * FINAL SCORE: You: {self.p1_score} Computer: {self.p2_score} * * * * * *")
                    print("* * * * * Game over! Better luck next time! * * * * * *  \n\n")
                    sleep(3)

                elif (round == 9) and self.p1_score > self.p2_score:
                    print(f"* * * * * * FINAL SCORE: You: {self.p1_score} Computer: {self.p2_score} * * * * * *")
                    print("* * * Congratulations! You won most of the games! * * * \n\n")
                    sleep(3)

                elif (round == 9) and self.p1_score == self.p2_score:
                    print(f"* * * * * * FINAL SCORE: You: {self.p1_score} Computer: {self.p2_score} * * * * * *")
                    print("* * * * * It is a tie! You both won the games! * * * * * \n\n")
                    sleep(3)
            self.p1_score = 0
            self.p2_score = 0
            repeat = input('Would you like to play again? (y/n): ')
            if repeat == 'y' or repeat == 'Y':
                print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \
                * * * *\n\n\n")
                pass
            else:
                sleep(0.5)
                print("\n Sad to see you leave. :( Bye bye")
                break


"""How to break a while true with a (y/N) at """
"""https://stackoverflow.com/questions/51446396/i-cant-break-out-of-while-true-loop-in-python-3-7"""

if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice([RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
