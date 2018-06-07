#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals, division
try:
    # Assume that we are on *nix or Mac - OS-specific code
    import termios
    import fcntl
    import os
    import sys

    def getch():
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            while 1:
                try:
                    sys.stdin.read(1)
                    break
                except IOError:
                    pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

except ImportError as e:
    try:
        # Opps, we might be on windows, try this one
        from msvcrt import getch
    except ImportError as e:
        # We can't make getch happen, just dump events to the screen
        getch = lambda: True


import argparse
import sc2reader
from sc2reader.events import *
from pprint import pprint

#function to parse through replay and get the JSON file to feed into Neural Network

def parseReplay(replay):

    print("=======================================================================================================================")
    #parse through the data for each player and obtain the relevant data to store
    for player in replay.players:
        #pprint(vars(player))
        #relevant features of each player to keep in storage
        buildingBuilt  = 0
        buildingKilled = 0
        armyBuilt      = 0
        armyKilled     = 0
        workerBuilt    = 0
        workerKilled   = 0
       
        #run this to observe all the units in each player and increment the values of the number of 
        #workers, army, and building units
        
        for unit in player.units:
            if(unit._type_class.is_army):
                armyBuilt += 1
            elif(unit._type_class.is_worker):
                workerBuilt += 1
            elif(unit._type_class.is_building):
                buildingBuilt += 1

        #run through for loop to increment the number of army, workers, and buildings killed for each player
        for unit in player.killed_units:
            if(unit._type_class.is_army):
                armyKilled += 1
            elif(unit._type_class.is_worker):
                workerKilled += 1
            elif(unit._type_class.is_building):
                buildingKilled += 1

        #output all of the relevant data for each player in the form of print statements
        print("pid: ", player.pid) #player ID
        print("team: ", player.team_id) #team ID
        print("result: ", player.result) #Result of the game for that player (Win/Loss)
        print("race: ", player.play_race) #Race that the player was playing as
        print("isHuman: ", player.is_human) #Whether the player is a player
        print("isObserver: ", player.is_observer) #Is the player a spectator
        print("isReferee: ", player.is_referee) #Is the player a referee in the game
        print("buildingBuilt: ", buildingBuilt) #number of buildings built by the player
        print("buildingKilled: ", buildingKilled) #Number of buildings destroyed
        print("armyBuilt: ", armyBuilt) #Amount of army built
        print("armyKilled: ", armyKilled) #Amount of army lost
        print("workerBuilt: ", workerBuilt) #number of workers established
        print("workerKilled: ", workerKilled) #Number of own workers dead in combat
        print("=======================================================================================================================")
    return


def main():
	#Parse through argumennt, which is description
    parser = argparse.ArgumentParser(
        description="""Step by step replay of game events; shows only the
        Initialization, Command, and Selection events by default. Press any
        key to advance through the events in sequential order."""
    )

    parser.add_argument('FILE', type=str, help="The file you would like to replay")
    parser.add_argument('--player', default=0, type=int, help="The number of the player you would like to watch. Defaults to 0 (All).")
    parser.add_argument('--bytes', default=False, action="store_true", help="Displays the byte code of the event in hex after each event.")
    args = parser.parse_args()

    #extract the replay file throgh the load_replay function
    replay = sc2reader.load_replay(args.FILE, debug=True)
    parseReplay(replay)


if __name__ == '__main__':
    main()
