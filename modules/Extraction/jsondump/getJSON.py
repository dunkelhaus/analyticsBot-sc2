#File that initiates the JSON file to gather the data

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals, division

try:
    # Assume that we are on *nix or Mac
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
import json
import glob
import sc2reader
from sc2reader.events import *
from pprint import pprint


#parse replay function that sets ups JSON
def parseReplay(replay):
    replayDic = {}
    idNum = 0

    for player in replay.players:
        if player is None:
            return {}
        buildingBuilt = 0
        buildingKilled = 0
        armyBuilt = 0
        armyKilled = 0
        workerBuilt = 0
        workerKilled = 0

        if player.units is not None:
            for unit in player.units:
                if (unit._type_class is None):
                    continue
                if (unit._type_class.is_army):
                    armyBuilt += 1
                elif (unit._type_class.is_worker):
                    workerBuilt += 1
                elif (unit._type_class.is_building):
                    buildingBuilt += 1

        if player.killed_units is not None:
            for unit in player.killed_units:
                if ( unit._type_class is None):
                    continue
                if ( unit._type_class.is_army):
                    armyKilled += 1
                elif (unit._type_class.is_worker):
                    workerKilled += 1
                elif (unit._type_class.is_building):
                    buildingKilled += 1

        entry = {}
        if player.pid is not None:
            entry['pid'] = player.pid
        if player.team_id is not None:
            entry['team'] = player.team_id
        if player.result is not None:
            entry['result'] = player.result
        if player.play_race is not None:
            entry['race'] = player.play_race

        entry['buildingBuilt'] = buildingBuilt
        entry['buildingKilled'] = buildingKilled
        entry['armyBuilt'] = armyBuilt
        entry['armyKilled'] = armyKilled
        entry['workerBuilt'] = workerBuilt
        entry['workerKilled'] = workerKilled

        replayDic[str(idNum)] = entry
        idNum = idNum + 1


    return replayDic


def main():
    dir = '../../../data/'
    rgen = sc2reader.load_replays(
        sc2reader.utils.get_files(
            path=dir,
            depth=-1,
            extension='SC2Replay'
        ),
        load_level=4
    )

    dic = {}
    id = 0
    for replay in rgen:
        dic[str(id)] = parseReplay(replay)
        id += 1

    with open('output.json', 'w') as outfile:
        json.dump(dic, outfile)


if __name__ == '__main__':
    main()
