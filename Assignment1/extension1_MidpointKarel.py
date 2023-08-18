"""
File: extension1_MidpointKarel.py
Name: Jumbo(Feat.Yu-Ching TA)
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    karel at midpoint and put one beeper
    """
    find_midpoint()
    go_to_midpoint()


def find_midpoint():
    """
    pre-condition:karel at(1,1),facing East
    post-condition:karel at middle of top
    """
    if not facing_north():
        turn_left()
    while front_is_clear():
        move()
        if front_is_clear():
            # foe even map
            move()
            turn_right()
            move()
            turn_left()


def go_to_midpoint():
    """
    pre-condition:karel at middle of top
    post-condition:karel at middle of bottom and put beeper
    """
    if not facing_south():
        turn_around()
    while front_is_clear():
        move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
