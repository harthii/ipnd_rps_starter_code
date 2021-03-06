#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    def __init__(self):
        self . round = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):  # save the learning method
        self . p1_nextmove = their_move
        self . p2_nextmove = my_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        choice = ' '
        while choice not in moves:
            choice = input("choose: rock, paper, or scissors? ").lower()
        return choice


class ReflectPlayer(Player):  # playes the other player move next.
    def move(self):
        self . round += 1
        if self . round == 1:
            return random . choice(moves)
        else:
            return self . p1_nextmove


class CyclePlayer(Player):
    def move(self):
        self . round += 1
        if self . round == 1:
            return random . choice(moves)
        else:
            k = self . p2_nextmove
            while k == self . p2_nextmove:
                k = random . choice(moves)
        return k


class Game:
    def __init__(self, p1, p2):
        self . p1 = p1
        self . p2 = p2
        self . p1_score = 0
        self . p2_score = 0

    def round_score(self, p1, p2):  # counts the score
        if p1 == p2:
            print("it's a tie")
        elif beats(p1, p2):
            self . p1_score += 1
            print("Player 1 wins")
        else:
            self . p2_score += 1
            print("You win")

    def play_round(self):
        move1 = self . p1 . move()
        move2 = self . p2 . move()
        print(f"\nPlayer 1 plays: {move1}     You play: {move2}\n")
        self . p1 . learn(move1, move2)
        self . p2 . learn(move2, move1)
        self . round_score(move1, move2)
        score = (
            f"\nPlayer1 score:{self . p1_score} \
                Your score:{self . p2_score}\n")
        print(score)

    def play_game(self):
        print("Game start!\n**Game ends when a player is 3 points ahead** \n")
        round = 1
        while -3 < (self . p1_score - self . p2_score) < 3:
            print(f"Round {round}:")
            self . play_round()
            round += 1
        if self . p1_score > self . p2_score:
            print("**YOU LOSE!**")
        else:
            print("**YOU WIN!!**")
        print("\nGAME OVER!")


if __name__ == '__main__':
    players = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    player = random.choice(players)
    game = Game(player, HumanPlayer())
    game . play_game()
