"""
File: extension3_triangular_checker.py
Name:
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""


def main():
    """
    To do:
    """
    i = 5
    a = i//2
    b = stancode(i % 2+2)
    if b:
        print('Answer 3: '+str(a))
    else:
        print('Answer 4:'+str(a))


def stancode(i):
    print('Answer 1:'+str(int(i+3.99)))
    i += 1
    a = i + stanCode(i)
    return a % 2 != 0


def stanCode(i):
    i /= 2
    print('Answer 2:'+str(i))
    return i


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
