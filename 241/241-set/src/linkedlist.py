class ListNode(object):
	def __init__(self, nextNode, word):
		self.next = nextNode
		self.word = word

class ListSet(object):
	def __init__(self, head):
		self.head = head
		dummyNode = ListNode(None, None)
		if self.head is None:
			self.length = 0
			self.head = dummyNode
		else:
			self.length = 1
			self.head.next = dummyNode

	def add(self, word):
		current = self.head
		while current.word is not None and current.next.word is not None and word > current.word and word > current.next.word:
			current = current.next

		if current.word is None: #head is empty
			self.length += 1
			current.word = word
			current.next = ListNode(None, None)
			return True
		elif word == current.word or word == current.next.word: #list contains word
			return False

		self.length += 1
		if self.head == current and word < current.word: #insert at head
			self.head = ListNode(current, word)
		elif current.next.word is None: #insert at end
			current = current.next
			current.word = word
			current.next = ListNode(None, None)
		else: #insert in middle
			current.next = ListNode(current.next, word)
		return True

	def contains(self, word):
		current = self.head
		while current.word is not None and word > current.word:
			current = current.next
		if word == current.word:
			return True
		else:
			return False

	def size(self):
		return self.length

	def printList(self):
		current = self.head
		listcontents = ""
		while current.word is not None:
			listcontents += current.word + ", "
			current = current.next
		print(listcontents)
		print("Size: " + str(self.length))

	def testList(self):
		self.printList()
		print("Size: " + str(self.size()))
		print("")

###### Executed Statements

def testListSet():
	#Test ListSet Initiation
	head = ListNode(None, "tiger")
	print(head.word)
	print(head.next)

	list1 = ListSet(head)
	print(list1.length)
	print(list1.size())

	list2 = ListSet(None)
	print(list2.length)
	print(list2.size())

	#Test ListSet add
	print (list2.add("tiger")) #case: add to null head
	list2.testList()
	print (list2.add("tiger")) #case: add duplicate to 1-node list
	list2.testList()
	print (list2.add("apple")) #case: insert before head
	list2.testList()
	print (list2.add("zucchini")) #case: insert at end
	list2.testList()
	print (list2.add("acacia")) #case: insert before head
	list2.testList()
	print (list2.add("movie")) #case: insert in middle
	list2.testList()
	print (list2.add("movie")) #case: duplicate in middle
	list2.testList()