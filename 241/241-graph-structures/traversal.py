### Input is adjacency list where index 0, 1, 2, 3... maps to A, B, C, D...

# startingNode is assumed to be the index of the starting node
def breadthFirstSearch(graph, startingNode):
	print('BFS:')

	visited = []
	willVisit = []
	for node in range(len(graph)):
		graph[node].sort() #make sure same-level nodes print in sorted order
		visited.append(False)

	willVisit.append(startingNode)
	visited[startingNode] = True

	while (len(willVisit) > 0):
		currentNode = willVisit.pop(0)
		print(indexToLetter(currentNode))
		for adjacent in graph[currentNode]:
			if not visited[adjacent]:
				visited[adjacent] = True
				willVisit.append(adjacent)

def depthFirstSearch(graph, startingNode):
	print('DFS:')
	visited = []
	willVisit = []
	for node in range(len(graph)):
		graph[node].sort(reverse=True) #make sure same-level nodes print in sorted order
		visited.append(False)

	willVisit.append(startingNode)

	while (len(willVisit) > 0):
		currentNode = willVisit.pop(len(willVisit) - 1)
		if not visited[currentNode]:
			visited[currentNode] = True
			print(indexToLetter(currentNode))
			for adjacent in graph[currentNode]:
				if not visited[adjacent]:
					willVisit.append(adjacent)

def indexToLetter(index):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	return alphabet[index]

def letterToIndex(letter):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	return alphabet.index(letter)

def alphaGraphToNum(arr):
	result = []
	for vertex in arr:
		convertedEdgeList = []
		for edge in vertex:
			convertedEdgeList.append(letterToIndex(edge.lower()))
		result.append(convertedEdgeList)
	return result

### Executables

graph1 = []
graph1.append(['b', 'd', 'i']) #A
graph1.append(['a', 'c', 'd', 'e']) #B
graph1.append(['b', 'e', 'f']) #C
graph1.append(['a', 'b', 'e', 'g']) #D
graph1.append(['b', 'c', 'd', 'f', 'g', 'h']) #E
graph1.append(['c', 'e', 'h']) #F
graph1.append(['d', 'e', 'h', 'i', 'j']) #G
graph1.append(['e', 'f', 'g', 'j']) #H
graph1.append(['a', 'g', 'j']) #I
graph1.append(['i', 'g', 'h']) #J

graph1num = alphaGraphToNum(graph1)
breadthFirstSearch(graph1num, letterToIndex('a'))
depthFirstSearch(graph1num, letterToIndex('a'))

graph2 = []
graph2.append(['b', 'e']) #A
graph2.append(['a', 'c', 'f']) #B
graph2.append(['b', 'd', 'g']) #C
graph2.append(['c', 'h']) #D
graph2.append(['a', 'f', 'i']) #E
graph2.append(['e', 'b', 'g', 'j']) #F
graph2.append(['f', 'c', 'h', 'k']) #G
graph2.append(['d', 'g', 'l']) #H
graph2.append(['e', 'm', 'j']) #I
graph2.append(['i', 'f', 'k', 'n']) #J
graph2.append(['j', 'g', 'l', 'o']) #K
graph2.append(['k', 'h', 'p']) #L
graph2.append(['i', 'n']) #M
graph2.append(['m', 'j', 'o']) #N
graph2.append(['n', 'k', 'p']) #O
graph2.append(['o', 'l']) #P

graph2num = alphaGraphToNum(graph2)
breadthFirstSearch(graph2num, letterToIndex('a'))
depthFirstSearch(graph2num, letterToIndex('a'))