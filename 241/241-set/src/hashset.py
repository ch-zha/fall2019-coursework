from linkedlist import *

class HashSet(object):
	def __init__(self, tablesize):
		self.length = 0
		self.tablesize = tablesize
		self.hashtable = []
		for i in range(tablesize):
			self.hashtable.append(ListSet(None))

	def hash(self, word):
		hash = 0
		while len(word) > 0:
			character = word[0]
			word = word[1:]
			hash = hash << 2
			hash += ord(character)
		# print(str(hash))
		return hash % self.tablesize

	def add(self, word):
		index = self.hash(word)
		# print(index)
		if (self.hashtable[index].add(word)):
			self.length += 1
			return True
		else:
			return False

	def contains(self, word):
		index = self.hash(word)
		return self.hashtable[index].contains(word)

	def size(self):
		return self.length

######## Executables

def testHashSet():
	set1 = HashSet(1000)
	set1.add("apple")
	set1.add("0123")

testHashSet()