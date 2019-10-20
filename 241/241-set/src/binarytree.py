class TreeNode(object):
	def __init__(self, word, left, right):
		self.word = word
		self.left = left
		self.right = right

class TreeSet(object):
	def __init__(self, root):
		self.root = root
		if self.root is None:
			self.root = TreeNode(None, None, None)
			self.length = 0
		else:
			self.length = 1

	def add(self, word):
		return self.addStep(self.root, word)

	def addStep(self, node, word):
		if node.word is None:
			node.word = word
			self.length += 1
			return True
		if node.word == word:
			return False

		if word < node.word:
			if node.left is None:
				node.left = TreeNode(word, None, None)
				self.length += 1
				return True
			else:
				return self.addStep(node.left, word)

		if word > node.word:
			if node.right is None:
				node.right = TreeNode(word, None, None)
				self.length += 1
				return True
			else:
				return self.addStep(node.right, word)

	def contains(self, word):
		return self.containsStep(self.root, word)

	def containsStep(self, node, word):
		if node.word is None:
			return False
		if node.word == word:
			return True

		if word < node.word:
			if node.left is None:
				return False
			else:
				return self.containsStep(node.left, word)

		if word > node.word:
			if node.right is None:
				return False
			else:
				return self.containsStep(node.right, word)

	def printTree(self):
		queue = []
		queue.append(self.root)
		tree = ""
		while len(queue) > 0:
			nextLeaf = queue.pop(0)
			if nextLeaf is not None and nextLeaf.word is not None:
				queue.append(nextLeaf.left)
				queue.append(nextLeaf.right)
				tree += nextLeaf.word + " "
			else:
				tree += "N/A "
		print(tree)
		print("Size: " + str(self.length))

	def size(self):
		return self.length

######### Executables

def testBinaryTree():
	treeNode = TreeNode("monday", None, None)
	tree1 = TreeSet(treeNode)
	tree2 = TreeSet(None)

	tree2.add("monday")
	tree2.add("banana")
	tree2.add("snail")
	tree2.add("lettuce")
	tree2.add("pine")
	tree2.add("zucchini")

	tree1.printTree()
	tree2.printTree()