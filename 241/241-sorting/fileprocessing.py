from sorts import *

import time
import sys

def readFile(filepath, sortmethod, outputfile):
	print("\nSorting words with " + sortmethod)
	time_output = ""
	size_output = ""
	words = []

	with open(filepath, 'r') as textFile:
		nextLine = textFile.readline()
		while nextLine != "":
			breakIndex = 0
			while nextLine != "":
				### Tokenize line
				while nextLine[breakIndex].isalnum():
					breakIndex += 1
				if breakIndex > 0:
					word = nextLine[0:breakIndex]
					words.append(word)
				nextLine = nextLine[breakIndex+1:]
				breakIndex = 0
			nextLine = textFile.readline()

	t = time.time()
	if sortmethod == "selection":
		selectionSort(words)
	elif sortmethod == "insertion":
		insertionSort(words)
	elif sortmethod == "heap":
		heapSort(words)
	elif sortmethod == "merge":
		mergeSort(words)
	elif sortmethod == "quick":
		quickSort(words)
	elif sortmethod == "library":
		words.sort()
	runtime = (time.time() - t) * 1000000000
	print(str(runtime))

	print('Writing...')
	with open(outputfile, 'a') as outputFile:
		outputFile.write(str(runtime) + "\n")

	return words

####### Executables
for i in range(10):
	readFile("pride-and-prejudice.txt", "selection", "selectionsortoutput.txt")
	readFile("pride-and-prejudice.txt", "insertion", "insertionsortoutput.txt")
	# readFile("pride-and-prejudice.txt", "heap", "heapsortoutput.txt")
	# readFile("pride-and-prejudice.txt", "merge", "mergesortoutput.txt")
	# readFile("pride-and-prejudice.txt", "quick", "quicksortoutput.txt")
	# readFile("pride-and-prejudice.txt", "library", "librarysortoutput.txt")