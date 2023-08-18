"""
File: extension1_factioral.py
Name: 
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    Find factorial
    """
    print('Welcome to stanCode master!')

    while True:
        result = 1
        n = int(input('Give ma number,and I will list the answer of factorial: '))
        if n == EXIT:
            print('- - - - - - See ya!- - - - - -')
            break
        else:
            while n > 0:
                result *= n  # n乘以所有小於n的數
                n -= 1    # 我忘了為什麼要-1
            print('Answer: ' + str(result))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
