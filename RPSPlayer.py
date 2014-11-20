#!/usr/bin/env python
__author__ = "William Ezekiel & Paul Council"
__date__ = "19 November 2014"
__version__ = "1.0"

#imports
import rpyc

""" An RPS game Player"""
class RPSPlayer(Player)

    # initializes RPSPlayer
    def __init__(self,name):
        self.name = name
        pass

    # play a round of RPS
    # Use past_moves to make a smart decision.
    def play(self,past_moves):
        all_moves = []
        opponent = None #later implement code to get opponent.
        while(True):
            move = strategy(all_moves)
            # add your move to 
            all_moves.append[move]
            opponent_move = 0
            #add their move
            all_moves.append[opponent_move]
                    
    # Returns 0 for rock, 1 for paper and 2 for scissors
    # past moves is a [blank] of you and your current opponent's
    # previous moves in the current game.
    def strategy(self,past_moves):
        # first move "scissors" (2)
        if len(past_moves) == 0:
            return 2	
        else:  # predict the next move and counter it
            opp_moves = []
            for i in range(0,len(past_moves),2):
                opp_moves.append(past_moves[i])
            counter_play = counter(predict(opp_moves))
            print(counter_play)
            return counter(predict(opp_moves))
        
    # Find the count of your opponents
    # previous moves and return the most likely move.
    def predict(self,opp_moves):
        play_count = []
        play_count.append(opp_moves.count(0)) #rock
        play_count.append(opp_moves.count(1)) #paper
        play_count.append(opp_moves.count(2)) #scissors
        return play_count.index(max(play_count))	#return most likely move. Will need to change later if moves are not numbers.

    # given a predicted opponents move, 
    # return the counter play.
    def counter(self,opp_move):
        if opp_move == 0:	#opponent plays rock
            return 1		#play paper
        elif opp_move ==1:	#opponent plays paper	
            return 2		#play scissors
        else:
            return 0		#opponent plasy scissors, play rock.
def main():
    #setPlayer(RPSPlayer())
    #ip address
    #host_ip = "abc123"
    #register(host_ip)
    play()
main()


