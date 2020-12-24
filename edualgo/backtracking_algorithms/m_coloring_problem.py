from __init__ import print_msg_box
import time 

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]for row in range(vertices)]

	def isSafe(self, v, colour, c):
		for i in range(self.V):
			if self.graph[v][i] == 1 and colour[i] == c:
				return False
		return True
	
	def graphColourUtil(self, m, colour, v):
		if v == self.V:
			return True

		for c in range(1, m + 1):
			if self.isSafe(v, colour, c) == True:
				colour[v] = c
				if self.graphColourUtil(m, colour, v + 1) == True:
					return True
				colour[v] = 0

	def graphColouring(self, m):
		colour = [0] * self.V
		if self.graphColourUtil(m, colour, 0) == None:
			return "Not Possible"
    
		return ' '.join(list(map(str,colour)))

def m_coloring(graph,m,hint=False):
	start = time.time() # start time
	if hint:
		m_coloring_hint()
	g = Graph(len(graph))
	g.graph = graph   # 2D graph matrix
	m = m           # m colors
	result = g.graphColouring(m)
	end = time.time() # end time
	print("Time Taken: ",end-start)
	return result


def m_coloring_hint():
    message="""
                                M Coloring Problem 
    ------------------------------------------------------------------------------------------
    Purpose : Given an undirected graph and a number m, determine if the graph can be colored with
    at most m colors such that no two adjacent vertices of the graph are colored with same color.

Method : Backtracking

Time Complexity :  O(m^V)
Space Complexity : O(V)

Hint :
The idea is to assign colors one by one to different vertices, starting from the vertex 0.
Before assigning a color, we check for safety by considering already assigned colors to the adjacent vertices.
If we find a color assignment which is safe, we mark the color assignment as part of solution.
If we do not a find color due to clashes then we backtrack and return false.

Pseudocode: 
Begin
if all vertices are checked, then
    return true
for all colors col from available colors, do
    if isValid(vertex, color, col), then
        add col to the colorList for vertex
        if graphColoring(colors, colorList, vertex+1) = true, then
            return true
        remove color for vertex
    done
    return false
End

Visualization:
Input:
2D Graph:  [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m color: 3

Input Graph Representaion:
    (D)---(C)
     |   / |
     |  /  |
     | /   |
    (A)---(B)

Solution: yes, it is 3 colorable 
    (2)---(3)
     |   / |
     |  /  |
     | /   |
    (1)---(2)
Output: 1 2 3 2

Learn More:
- Backtracking - https://en.wikipedia.org/wiki/Backtracking
- Graph_coloring - https://en.wikipedia.org/wiki/Graph_coloring

    """
    print_msg_box(message)


# print(m_coloring([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]],3,True))


