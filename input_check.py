import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
	# There is no input checking: non-numeric input raises an error, and guesses
	# outside the displayed 1-9 range are still accepted.
	guess = int(input("Guess a number between 1 and 9: "))
	number_of_guesses += 1
	if guess == number:
		break
print(f"You needed {number_of_guesses} guesses to guess the number {number}")