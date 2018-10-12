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
        self.round=0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.p1_nextmove= their_move
        self.p2_nextmove= my_move



class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):        
        return input("choose: Rock, paper, or scissors?")

class ReflectPlayer(Player):
    def move(self):
        self.round+=1 
        if self.round==1:
            
            return random.choice(moves)
        else:
            return self.p1_nextmove
          




class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score=0
        self.p2_score=0

    def round_score(self,p1, p2):  # counts the score
        if p1==p2:
            print("it's a tie")
        elif beats(p1,p2)== True:
            self.p1_score+=1
            print("player 1 wins")
        else: 
            self.p2_score+=1    
            print("player 2 wins")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        
        #-----------------------------
        self.round_score(move1,move2)
        score=(f"player1 score={self.p1_score}  player2 score={self.p2_score}") 
        print(score)
            

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(ReflectPlayer(), HumanPlayer())
    game.play_game()
