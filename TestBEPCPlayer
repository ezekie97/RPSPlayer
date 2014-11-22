__author__= "William Ezekiel & Paul Council"
__date__ = " 22 November 2014"
__version__= "0.1"

#imports
import BEPCPlayer
import Message

def main():
    """
    Test BEPCPlayer
    """
    player = BEPCPlayer.BEPCPlayer()
    match(player)

    

def match(player):
    """
    Replicate a match of  5 rounds of RPS game
    :param player the player
    """
    player.notify(Message.Message.get_match_start_message((player,None)))

    #Begin round
    start_round(player)

    # prints 2, no moves made yet
    play = player.play()
    print("Played: ",play)

    # End round
    # player 1 plays scissors. player 2 plays rock, rock wins.
    end_round(player,play,0,2)
    display_stats(player)   # [2]
                            # [0]
                            # [0]

    prompt()
    
    start_round(player)
    # since rock is now the most common move of the opponent.
    # play paper. print 1
    play = player.play()
    print("Played: ",play)

    # End round
    # player 1 plays paper. player 2 plays rock, paper wins.
    end_round(player,play,0,1)
    display_stats(player)   # [2,1]
                            # [0,0]
                            # [0,1]

    prompt()

    start_round(player)
    # since rock is now the most common move of the opponent.
    # play paper. print 1
    play = player.play()
    print("Played: ",play)

    # End round
    # player 1 plays paper. player 2 plays scissors, scissors wins.
    end_round(player,play,2,0)
    display_stats(player)   # [2,1,1]
                            # [0,0,2]
                            # [0,1,0]

    prompt()

    start_round(player)
    # since rock is now the most common move of the opponent.
    # play paper. print 1
    play = player.play()
    print("Played: ",play)

    # End round
    # player 1 plays paper. player 2 plays scissors, scissors wins.
    # Uh-Oh.....
    end_round(player,play,2,0)
    display_stats(player)   # [2,1,1,1]
                            # [0,0,2,2]
                            # [0,1,0,0]

    prompt()

    start_round(player)
    # since rock is now the most common move of the opponent.
    # play paper. print 1
    play = player.play()
    print("Played: ",play)

    # End round
    # player 1 plays paper. player 2 plays scissors, scissors wins.
    # Looks like our opponent is figuring us out.
    end_round(player,play,2,0)
    display_stats(player)   # [2,1,1,1,1]
                            # [0,0,2,2,2]
                            # [0,1,0,0,0]

    prompt()

    start_round(player)
    # since rock is now the most common move of the opponent.
    # play paper. print 1
    play = player.play()
    print("Played: ",play)

    # End round
    # player 1 plays rock. player 2 plays scissors, rock wins.
    # We finally won again, but lost a few on the way.
    # So what if our opponent figures out to guess in this fashion
    # and is able to predict when we will switch???

    #however we do know that our current algorith does function properly.
    end_round(player,play,2,1)
    display_stats(player)   # [2,1,1,1,1,0]
                            # [0,0,2,2,2,2]
                            # [0,1,0,0,0,1]

    prompt()

    # not only that but we lost the match.
    player.notify(Message.Message.get_match_end_message((player,None),1))
    print("Testing Complete, Match Over")
    
def display_stats(player):
    """
    Print this plays past moves, its opponents moves
    and this players current win record
    :param player the player
    """
    print(player.get_past_moves())  
    print(player.get_opp_moves())   
    print(player.get_win_record())  
    
def start_round(player):
    """
    Start a round
    :param player the player
    """
    player.notify(Message.Message.get_round_start_message((player,None)))

def end_round(player,move,move_opp,win):
    """
    End a round
    :param player the player
    :param move the players move
    :param opp_move the opponents move
    :param win integer representing who won
    """
    player.notify(Message.Message.get_round_end_message((player,None),(move,move_opp),win))

def prompt():
    """
    Prompt the player asking them to press enter
    if they want to move on. This spaces the printed data and prevents all
    of it from printing at once.
    """
    input("Press Enter to continue Tests")
    print("\n\n\n")
