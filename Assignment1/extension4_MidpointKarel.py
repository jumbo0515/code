"""
File: extension4_MidpointKarel.py
Name:
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
    move_to_corner()
    find_beeper()
    # put_back()


def move_to_corner():
    """
    pre-condition:karel at(1,1),facing East
    post-condition:karel at lower right corner and put beeper are spaced ,facing East
    """
    put_beeper()
    while front_is_clear():
        if on_beeper():
            move()
        elif front_is_clear():
            move()
            put_beeper()


def find_beeper():
    turn_around()
    move()
    while front_is_clear():
        if not on_beeper():
            move()
        else:
            pick_beeper()
            turn_around()
            put_beeper()


def put_back():
    while front_is_clear():
        move()
        if on_beeper():
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
