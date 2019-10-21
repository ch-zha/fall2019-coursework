from linkedlist import *
from binarytree import *
from hashset import *

import time
import sys

def readFile(filepath, datatype, outputfile):
	print("\nAdding words to " + datatype)
	time_output = ""
	size_output = ""

	if datatype == "linkedlist":
		newSet = ListSet(None)
	elif datatype == "bintree":
		newSet = TreeSet(None)
	elif datatype == "hash":
		newSet = HashSet(1000)
	else:
		return None

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
					t = time.time()
					newSet.add(word)
					addtime = (time.time() - t) * 1000000000
					time_output += str(addtime) + "\n"
					size_output += str(newSet.size()) + "\n"
				nextLine = nextLine[breakIndex+1:]
				breakIndex = 0
			nextLine = textFile.readline()

	with open(outputfile, 'a') as outputFile:
		outputFile.write("Times:" + "\n" + time_output + "\n\n")
		outputFile.write("Sizes:" + "\n" + size_output + "\n\n")

	print("No. words added: " + str(newSet.size()))
	return newSet

def findDiff(filepath, comparisonSet, outputfile):
	print("\nFinding difference...")

	diff = ""
	diffCount = 0
	totalCount = 0
	worstCase = 0
	bestCase = sys.maxint
	avgCase = 0

	with open(filepath, 'r') as textFile:
		nextLine = textFile.readline()
		while nextLine != "":
			breakIndex = 0
			while nextLine != "":
				### Tokenize line
				while breakIndex < len(nextLine) and nextLine[breakIndex].isalnum():
					breakIndex += 1
				if breakIndex > 0:
					totalCount += 1
					word = nextLine[0:breakIndex]
					### Update record times
					t = time.time()
					containsWord = comparisonSet.contains(word)
					searchtime = (time.time() - t) * 1000000000
					if searchtime < bestCase:
						bestCase = searchtime
					if searchtime > worstCase:
						worstCase = searchtime
					avgCase += searchtime
					###
					if not containsWord:
						diff += word + ", "
						diffCount += 1
				nextLine = nextLine[breakIndex+1:]
				breakIndex = 0
			nextLine = textFile.readline()
	print(diff)
	print("No. words not found: " + str(diffCount))
	print("Best Time: " + str(bestCase))
	print("worst Time: " + str(worstCase))
	print("Avg. Time: " + str(avgCase/totalCount))

	with open(outputfile, 'a') as outputFile:
		outputFile.write("No. words not found: " + str(diffCount) + "\n")
		outputFile.write("Best Time: " + str(bestCase) + "\n")
		outputFile.write("worst Time: " + str(worstCase) + "\n")
		outputFile.write("Avg. Time: " + str(avgCase/totalCount) + "\n")

def readFileToAllTypes(filepath):
	pass

def findDiffInAllTypes(filepath):
	pass

####### Executables
# for i in range(10):
i = 0
listoutputfile = "linkedlist" + str(i) + ".txt"
treeoutputfile = "bintree" + str(i) + ".txt"
hashoutputfile = "hashtable" + str(i) + ".txt"

listset = readFile('pride-and-prejudice.txt', 'linkedlist', listoutputfile)
findDiff('words-shuffled.txt', listset, listoutputfile)

treeset = readFile('pride-and-prejudice.txt', 'bintree', treeoutputfile)
findDiff('words-shuffled.txt', treeset, treeoutputfile)

hashset = readFile('pride-and-prejudice.txt', 'hash', hashoutputfile)
findDiff('words-shuffled.txt', hashset, hashoutputfile)