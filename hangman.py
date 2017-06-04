#!/usr/bin/python3

import sys
import random

def checkLetter(inputLetter, secretWord, letterRevealed):
	charList = list(secretWord)
	for i in range(0,len(secretWord)):
			# check whether the letter is matched or not
			if inputLetter == charList[i]:
				letterRevealed[i] = True
	return letterRevealed

def printRevealingList(secretWord, letterRevealed):
	charList = list(secretWord)
	for i in range(0,len(secretWord)):
		if letterRevealed[i]:
			print ("%s " % charList[i], end='', flush=True)
		else:
			print ("_ ", end='', flush=True)
	print('\n')

def main():
	wordList = []
	letterRevealed = []
	letterGuessed = []

	# importing all the words from words.txt

	print("Loading word list from file...")

	f = open("words.txt", "r")
	for line in f:
		 for word in line.split():
		 	wordList.append(word)

	f.close()

	print("%d words loaded.\n" % len(wordList))

	# picking a random word from the list

	wordIndex = random.randint(0, len(wordList))
	secretWord = wordList[wordIndex]

	# print(secretWord)

	letterRevealed = [False] * len(secretWord)
	avaiableGuesses = 6
	noOfRemianingLetter = len(secretWord)

	print("Welcome to the game Hangman!\nI am thinking of a word that is %i letters along\n------------------------------" % len(secretWord))

	while True:
		print("You have %i guesses left!" % avaiableGuesses)
		inputLetter = input("Please guess a letter: ")

		letterGuessed.append(inputLetter)
		print(*letterGuessed, sep='')

		letterRevealed = checkLetter(inputLetter, secretWord, letterRevealed)
		printRevealingList(secretWord, letterRevealed)

		if letterRevealed.count(False) == noOfRemianingLetter:
			avaiableGuesses -= 1

		noOfRemianingLetter = letterRevealed.count(False)

		if noOfRemianingLetter == 0:
			print("You win the game!")
			break

		
		if avaiableGuesses == 0:
			print("You lose the game!")
			print("The secret word is", secretWord)
			break


if __name__ == "__main__":
	main()