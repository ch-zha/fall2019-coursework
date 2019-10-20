# Complexity: O(n^2) with respect to the number of vertices
def adjMatToList(arr):
	# Expect arr to be 2D matrix where inner array values are either truthy or falsy (0 or 1)
	adjList = []
	for innerlist in arr:
		edges = []
		for vertex in range(len(innerlist)):
			if innerlist[vertex] == True:
				edges.append(vertex)
		adjList.append(edges)
	return adjList

# Complexity: O(m) with respect to the number of edges
def adjListToIncidence(arr):
	arrcopy = [] # copy original array for deletion
	vertices = []
	for vertex in range(len(arr)):
		vertices.append([])
		arrcopy.append(arr[vertex][:])
	for vertex in range(len(arrcopy)):
		for endpoint in arrcopy[vertex]:
			for incidenceVertex in vertices: # add new edge column
				incidenceVertex.append(0)
			edgeswritten = len(vertices[0])
			if endpoint == vertex: # self-loop
				vertices[vertex][edgeswritten - 1] = 2
			else:
				vertices[vertex][edgeswritten - 1] = 1
				vertices[endpoint][edgeswritten - 1] = 1
				arrcopy[endpoint].remove(vertex)
	return vertices

# Complexity: O(nm) with respect to the number of vertices and the number of edges
def incidenceToAdjList(arr):
	edges = []
	edgesCounting = []
	for vertex in range(len(arr)):
		edges.append([]) # Create entry for each vertex
	for edge in range(len(arr[0])):
		edgesCounting.append([]) # Create entry for each edge
	for vertex in range(len(arr)):
		for edge in range(len(arr[vertex])):
			if arr[vertex][edge] > 0:
				edgesCounting[edge].append(vertex)
			if arr[vertex][edge] == 2: # if self-loop
				edgesCounting[edge].append(vertex)
	for edge in edgesCounting: # copy edges into adj list
		edges[edge[0]].append(edge[1])
		if edge[0] != edge[1]:
			edges[edge[1]].append(edge[0])
	return edges

### Executables

## SET 1 (2 edges + 1 self-loop) ##
adjmat1 = [[0, 1, 0], [1, 0, 1], [0, 1, 1]]
adjlist1 = adjMatToList(adjmat1)
assert adjlist1 == [[1], [0, 2], [1, 2]], str(adjlist1)

incidence1 = adjListToIncidence(adjlist1)
assert incidence1 == [[1, 0, 0], [1, 1, 0], [0, 1, 2]], str(incidence1)

adjlist2 = incidenceToAdjList(incidence1)
assert adjlist2 == [[1], [0, 2], [1, 2]], str(adjlist2)

## SET 2 (No Edges) ##
adjmat1 = [[0, 0], [0, 0]]
adjlist1 = adjMatToList(adjmat1)
assert adjlist1 == [[], []], str(adjlist1)

incidence1 = adjListToIncidence(adjlist1)
assert incidence1 == [[], []], str(incidence1)

adjlist2 = incidenceToAdjList(incidence1)
assert adjlist2 == [[], []], str(adjlist2)

## Set 3 (All Edges) ##
adjmat1 = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
adjlist1 = adjMatToList(adjmat1)
assert adjlist1 == [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]], str(adjlist1)

incidence1 = adjListToIncidence(adjlist1)
assert incidence1 == [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0, 1, 1]], str(incidence1)

adjlist2 = incidenceToAdjList(incidence1)
assert adjlist2 == [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]], str(adjlist2)