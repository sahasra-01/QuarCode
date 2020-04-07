# Python program for Breadth First Search (BFS) algorithm - Sahasra Ranjan

class Graph:

	def __init__(self, n_vertices):
		self.V = n_vertices
		self.adj = [[] for col in range(self.V)]
	
	def addEdge(self, v, w):
		self.adj[v].append(w)

	def BFS(self, s):
		visited = [False]*self.V
		path = []

		queue = []
		visited[s] = True

		queue.append(s)

		while queue:
			s = queue[0]
			path.append(s)
			queue.pop(0)

			for i in self.adj[s]:
				if visited[i] == False:
					visited[i] = True
					queue.append(i)
			print(queue)

		print(path)


n = int(input())
g = Graph(n)		# Instantiation, object g of class Graph

# Graph is represented as 2D array(list here)
# g[i][j] = 0, means no edge
# else: g[i][j] = w  means an egde from i to j of weight w (directed)
# here since undirected, g[i][j] = g[j][i] = w
for i in range(n):
	edge = int(input())
	for t in range(edge):
		t1, t2 = input().split()
		j = int(t1)
		w = int(t2)
		g.addEdge(i, j)	

g.BFS(0)

