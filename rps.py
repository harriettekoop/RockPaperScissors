#!/usr/bin/env python3

# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round.

import random
import string
moves = ["rock", "paper", "scissors"]

# The Player class is the parent class for all of the Players
# in this game


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def tie(one, two):
    return (one == two)


class Player:
    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    # returns rock, paper or scissors at random
    def move(self):
        move = random.choice(moves)
        return move


class HumanPlayer(Player):
    def move(self):
        move = input("Rock, paper or scissors?")
        move = move.lower()
        if move in moves:
            return move
        else:
            print("Please type in rock, paper or scissors")
            self.move()


class ReflectPlayer(Player):
    def __init__(self):
        self.count_moves = 0

    # sla op wat de move is van de tegenstander als volgende move
    def learn(self, my_move, their_move):
        self.my_next_move = their_move

    # return opgeslagen move (van de ander) als eigen move
    # MITS het niet de eerste move is
    def move(self):
        if self.count_moves == 0:
            move = random.choice(moves)
            self.count_moves += 1
            return move
        else:
            return self.my_next_move


class CyclePlayer(Player):
    def __init__(self):
        self.count_moves = 0

    # sla op welke move ik zelf had
    def learn(self, my_move, their_move):
        self.my_move = my_move

    # return volgende move in de lijst met moves
    # MITS het niet de eerste move is
    def move(self):
        if self.count_moves == 0:
            move = random.choice(moves)
            self.count_moves += 1
            return move
        else:
            # zoek de plek van de huidige self.my_move in de lijst
            index = moves.index(self.my_move)
            # de move wordt de volgende in de lijst met moves
            move = moves[(index + 1) % 3]
            return move


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move().lower()
        move2 = self.p2.move().lower()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("Player 1 wins the round!")
            self.score_p1 += 1
        elif tie(move1, move2):
            print("Game Tied!")
        else:
            print("Player 2 wins the round!")
            self.score_p2 += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        return self.score_p1, self.score_p2

    def play_game(self):
        print("Welcom to Rock Paper Scissors! We play 'best in three'")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(f"Round {round}: \nPlayer 1 Score {self.score_p1} "
                  f" \nPlayer 2 Score {self.score_p2}")
        if self.score_p1 > self.score_p2:
            print("Player 1 wins the game!")
        else:
            print("Player 2 wins the game!")
        print("Game over!")


if __name__ == '__main__':
    # maak een nieuwe game-object aan
    game = Game(HumanPlayer(), RockPlayer())
    # voer play_game method uit met deze nieuwe game als object
    game.play_game()
