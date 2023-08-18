"""
File: hailstone.py
Name:Jumbo
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

EXIT = 1


def main():
    """
    The execution of the Hailstone sequence, defined by Douglas
    Hofstadter.
    if n is odd ,multiply N by 3 and add 1
    if n is even,Divide N by 2
    """
    print('This program computes Hailstone sequences')
    x = int(input('Enter a number: '))
    step = 0
    while True:
        if x == EXIT:
            print('It took ' + str(step) + ' steps to reach 1')
            break
        if x % 2 == 0:
            even = x // 2
            print(str(x) + ' is even,so I take off: ' + str(even))
            x = even
        else:
            odd = 3 * x + 1
            print(str(x) + ' is odd,so I make 3n+1: ' + str(odd))
            x = odd
        step += 1





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
