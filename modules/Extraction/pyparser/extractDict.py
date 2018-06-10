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
import sc2reader
from sc2reader.events import *
from pprint import pprint

def parseReplay(replay):
    dic = vars(replay)
    pprint(dic) 
    return


def main():
    parser = argparse.ArgumentParser(
        description="""Step by step replay of game events; shows only the
        Initialization, Command, and Selection events by default. Press any
        key to advance through the events in sequential order."""
    )

    parser.add_argument('FILE', type=str, help="The file you would like to replay")
    parser.add_argument('--player', default=0, type=int, help="The number of the player you would like to watch. Defaults to 0 (All).")
    parser.add_argument('--bytes', default=False, action="store_true", help="Displays the byte code of the event in hex after each event.")
    args = parser.parse_args()

    for filename in sc2reader.utils.get_files(args.FILE):
        replay = sc2reader.load_replay(filename, debug=True)
        parseReplay(replay)

if __name__ == '__main__':
    main()
