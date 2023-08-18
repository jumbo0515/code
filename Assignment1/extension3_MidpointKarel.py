"""
File: extension3_MidpointKarel.py
Name: Jumbo
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
    if front_is_clear():
        move_to_corner()
        find_midpoint()
    else:
        # for1x1
        put_beeper()


def move_to_corner():
    """
    pre-condition:karel at(1,1),facing East
    post-condition:karel at lower right corner and put beeper on line except corner ,facing East
    """
    move()
    while front_is_clear():
        put_beeper()
        move()


def find_midpoint():
    """
    pre-condition:karel at lower right corner and put beeper on line except corner ,facing East
    post-condition:karel at midpoint with beeper ,facing South
    """
    turn_around()
    move()
    if on_beeper():
        pick_beeper()
    while front_is_clear():
        move()
        if not on_beeper():
            turn_around()
            move()
            if not on_beeper():
                turn_right()
            else:
                pick_beeper()
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
