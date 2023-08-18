"""
File: MidpointKarel.py
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
        job()
    else:
        # for1x1
        put_beeper()


def job():
    """
    pre-condition:karel at (1,1),facing East
    post-condition:karel find midpoint and put beeper
    """
    put_beeper_on_diagonal()
    go_lower_right_corner()
    find_midpoint()
    go_lower_left_corner()
    pick_beeper_on_diagonal()
    go_lower_right_corner()
    go_midpoint()


def put_beeper_on_diagonal():
    """
    pre-condition:karel at (1,1),facing East
    post-condition:karel at upper right corner and put beeper on diagonal,facing East
    """
    put_beeper()
    while front_is_clear():
        move()
        turn_left()
        move()
        turn_right()
        put_beeper()


def go_lower_right_corner():
    """
    pre-condition:karel at upper right corner,facing East
    post-condition:karel at lower right corner ,facing South
    """
    if not facing_south():
        turn_right()
    while front_is_clear():
        move()


def find_midpoint():
    """
    pre-condition:karel at lower right corner ,facing South
    post-condition:karel find midpoint and put beeper
    """
    if not facing_west():
        turn_right()
    while front_is_clear():
        # find the beeper placed on the diagonal
        if on_beeper():
            if not facing_south():
                turn_left()
            while front_is_clear():
                move()
                if not front_is_clear():
                    put_beeper()
        else:
            move()
            # for even map
            if on_beeper():
                if not facing_south():
                    turn_left()
                while front_is_clear():
                    move()
                    if not front_is_clear():
                        put_beeper()
            turn_right()
            if front_is_clear():
                # for2x2
                move()
                turn_left()
            else:
                put_beeper()


def go_lower_left_corner():
    """
    pre-condition:karel find middle
    post-condition:karel at (1,1),facing East
    """
    if not facing_west():
        turn_right()
    while front_is_clear():
        move()
    if not facing_east():
        turn_around()


def pick_beeper_on_diagonal():
    """
    pre-condition:karel at (1,1),facing East
    post-condition:karel at upper right corner and pick beeper on diagonal,facing East
    """
    pick_beeper()
    while front_is_clear():
        move()
        turn_left()
        move()
        turn_right()
        pick_beeper()


def go_midpoint():
    """
   pre-condition:karel at lower right corner ,facing South
   post-condition:karel find middle
   """
    if not facing_west():
        turn_right()
    while not on_beeper():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
