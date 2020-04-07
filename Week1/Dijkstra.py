# Python program for Dijkstra's algorithm - Sahasra Ranjan
maxint = 999999999

class Graph():

	# Constructor, Note: def of graph ( do not use [[0]*n]*n, this will throw error while assigning values)
	# [[0]*n]*n  returns same reference to all the lists
	def __init__(self, vertices):
		self.V = vertices
		self.graph =[[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    # Return which index to select for next iteration
	def minDistance(self, dist, sptSet):
		min = maxint

		for v in range(self.V):
			if (sptSet[v] == False and dist[v] < min):
				min = dist[v]
				min_index = v

		return min_index


	# Dijksta's Algorithm
	def dijkstra(self, src):
		dist = [maxint]*self.V
		sptSet = [False]*self.V

		dist[src] = 0

		# V-1 loop to assign min distance all the vertices from source
		for count in range(self.V-1):
			u = self.minDistance(dist, sptSet)

			sptSet[u] = True

			# If shorter than previously assigned path
			for v in range(self.V):
				if (sptSet[v] == False and self.graph[u][v]!=0 and dist[u] != maxint and dist[u] + self.graph[u][v] < dist[v]):
					dist[v] = dist[u] + self.graph[u][v]

		print (dist)


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
		g.graph[i][j] += w
		g.graph[j][i] += w	

g.dijkstra(0)
