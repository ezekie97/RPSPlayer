#!/usr/bin/env python
__author__ = "William Ezekiel & Paul Council"

__date__ = "19 November 2014"

__version__ = "0.1"

#imports
import rpyc

""" An RPS game Player"""
class RPSPlayer():

    def __init__(self,host,port):
        """ Connect to the framework where the tournament
        is being hosted
        :param host name/ip address of machine with framework
        :param port the port number of the service on the
            machine with the framework
        """
        #self.connection = connectFramework(host,port)
        
    def connectFramework(self,host,port):
        """ Connect to the framework where the tournament
        is being hosted
        :param host name/ip address of machine with framework
        :param port the port number of the service on the
            machine with the framework
        :return an rpyc connection
        """
        return rpyc.connect(host,port)

    def play(self,earlierPlays):
        """ Make a move based on opponents previous moves if applicable
            :param earlierPlays the previous moves of your opponent.
            :return a move (currently represented as a string)
        """
        #if no play has been made previously
        if earlierPlays == []:
            return "scissors"   #for now a string, will be represented properly when we know the full functionality of the framework.
        elif earlierPlays[-1] == earlierPlays[-2]:
            #if previous two moves were the same, expect a trap.
            #if they played rock then rock, they want you to play
            #paper, counter by playing rock when they throw scissors
            #expecting your paper. 
               return earlierPlays[-1]
        else:
            #probability opponent uses rock next
            probRock = earlierPlays.count("rock")/len(earlierPlays)
            #probability opponet uses scissors next
            probScissors = earlierPlays.count("scissors")/len(earlierPlays)
            #probability opponent uses paper next
            probPaper = earlierPlays.count("paper")/len(earlierPlays)

            nextPlay = max(probRock,probScissors,probPaper)

            if nextPlay == probRock:
                return "rock"
            if nextPlay == probScissors:
                return "scissors"
            if nextPlay == probPaper:
                return "paper"
            
            
            
        
        
    
        
        
