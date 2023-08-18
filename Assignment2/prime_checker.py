"""
File: prime_checker.py
Name:Jumbo
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	find prime number
	"""
	print('Welcome to the prime checker!')

	while True:
		n = int(input('n: '))
		a = 1
		if n != EXIT:
			while True:
				a += 1
				if n == a:  # check divide
					print(str(n) + ' is a prime number')
					break
				if n % a == 0:
					print(str(n) + ' is not a prime number')
					break
		else:
			print('Have a good one!')
			break


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
