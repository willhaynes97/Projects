#  File: TopoSort.py

#  Description: Breadth-First search

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
      
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # deleteVertex
  def deleteVertex(self, vertexLabel):
    v = self.getIndex(vertexLabel)
    xVert = len(self.Vertices)

    # remove column
    for i in range(xVert):
      for j in range(v, xVert - 1):
        self.adjMat[i][j] = self.adjMat[i][j + 1]
      self.adjMat[i].pop()

    # remove row
    self.adjMat.pop(v)

    for vertex in self.Vertices:
      if vertex.label == vertexLabel:
        self.Vertices.remove(vertex)

  def getNeighbors(self, vertexLabel):
    neighbors = []
    v = self.getIndex(vertexLabel)
    for i in range(len(self.Vertices)):
      if (self.adjMat[v][i] > 0):
        neighbors.append(self.Vertices[i])
    return neighbors


  # cycle checker
  def hasCycle(self):
    for i in self.Vertices:
      if self.cyclehelper(None, i):
        return True
      for j in range(len(self.Vertices)):
        (self.Vertices[j]).visited = False
    return False

  def cyclehelper(self, previous, v):
    if v.wasVisited() == True:
      return True
    v.visited = True
    neighbors = self.getNeighbors(v.label)
    if previous in neighbors:
      neighbors.remove(previous)
    if len(neighbors) == 0:
      return False
    for neighbor in neighbors:
      return self.cyclehelper(v, neighbor)


  def get_in_degree_list(self):
    # Count in_degree of all vertices
    in_degree_list = []
    for i in self.Vertices:
      idx = self.getIndex(i.label)
      degree = 0
      for j in range (len (self.adjMat[idx])):
        if (self.adjMat[j][idx] == 1):
          degree += 1
      in_degree_list.append(degree)
    return in_degree_list
  
  def current_level_topo(self):
    current_degree_check = 0
    current_degree_list = []
    degree_list = self.get_in_degree_list()
    for i in range(len(degree_list)):
      if (degree_list[i] == current_degree_check):
        current_degree_list.append((self.Vertices[i]).label)

    return current_degree_list

  def isEmpty(self):
    if len(self.Vertices) == 0:
      return True
    else:
      return False

  def toposort(self):
    if self.hasCycle():
      return None

    nVerts = len(self.Vertices)
    
    copyGraph = Graph()
    for v in self.Vertices:
      copyGraph.addVertex(v.label)
    for i in range(nVerts):
      for j in range(nVerts):
        copyGraph.addDirectedEdge(i, j, self.adjMat[i][j]) 
    
    final_list = []
    while (copyGraph.isEmpty() != True):
      cur_level = copyGraph.current_level_topo()
      cur_level = sorted(cur_level)
      final_list.append(cur_level)
      for vertex in cur_level:
        copyGraph.deleteVertex(vertex)

    combine_final_list = []
    for i in range(len(final_list)):
      for j in range(len(final_list[i])):
        combine_final_list.append(final_list[i][j])
    
    return combine_final_list
  
      
  



def main():
  # create a Graph object
  topos = Graph()

  # open file for reading
  inFile = open ("./topo.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())


  for i in range (numVertices):
    vertex = (inFile.readline()).strip()

    topos.addVertex (vertex)

  # read the edges
  numEdges = int ((inFile.readline()).strip())


  for i in range (numEdges):
    edge = (inFile.readline()).strip()

    edge = edge.split()
    start = topos.getIndex(edge[0])
    finish = topos.getIndex(edge[1])
    weight = 1
    topos.addDirectedEdge (start, finish, weight)

 """ # print the adjacency matrix
  print ("\nAdjacency Matric")
  for i in range (numVertices):
    for j in range (numVertices):
      print (topos.adjMat[i][j], end = ' ')
    print ()
  print ()"""

  

  # Test for cyclicality
  print()
  result = topos.hasCycle()
  if result == False:
    print("Result is False")
  else:
    print("Result is True")
  # Test topological sort
  print ("\nTopological Sort")
  sortedlist = topos.toposort()
  print (sortedlist)
  


main()

