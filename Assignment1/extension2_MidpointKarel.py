"""
File: extension2_MidpointKarel.py
Name: Jumbo(Feat.Jenny TA)
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
    put_beeper_in_corner()
    find_midpoint()
    go_to_midpoint()
    for_2x2()


def put_beeper_in_corner():
    """
    pre-condition:karel at(1,1),facing East
    post-condition:karel at lower right corner and put beeper on corner ,facing East
    """
    put_beeper()
    while front_is_clear():
        move()
        if not front_is_clear():
            put_beeper()


def find_midpoint():
    """
   pre-condition:karel at lower right corner and put beeper on corner ,facing East
   post-condition:karel at(1,1)and put beeper on midpoint ,facing West
   """
    if not facing_west():
        turn_around()
    while front_is_clear():
        move()
        if on_beeper():
            turn_around()
            pick_beeper()
            move()
            put_beeper()


def go_to_midpoint():
    """
   pre-condition:karel at(1,1)and put beeper on midpoint ,facing West
   post-condition:karel at midpoint with beeper ,facing South
   """
    turn_around()
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            if facing_east():
                turn_right()
            if facing_west():
                turn_left()


def for_2x2():
    """
    in 2x2 map,one more on the right,need pick up
    """
    if facing_west():
        turn_around()
        move()
        pick_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()








# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
