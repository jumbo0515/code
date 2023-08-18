"""
File: quadratic_solver.py
Name:Jumbo
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
import math


def main():
    """
    asks 3 inputs (a, b, and c) from users to compute the roots of equation: ax^2 + bx + c = 0
    judgment discriminant : b^2 - 4ac  it greater than zero
    """

    print('standCode Quadratic Solver!')
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    y = b * b - 4 * a * c
    if y >= 0:
        x1 = (-b + math.sqrt(y)) / (a * 2)
        x2 = (-b - math.sqrt(y)) / (a * 2)
        if y == 0:
            print('One root: ' + str(x1))
        elif y > 0:
            print('Two roots: ' + str(x1), str(x2))
    else:
        print('No real roots')


# print('The roots:'+str(x))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
