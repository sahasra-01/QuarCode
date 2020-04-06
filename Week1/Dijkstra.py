# Python program for Dijkstra's algorithm - Sahasra Ranjan
maxint = 999999999

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0]*vertices]*vertices


	def minDistance(self, dist, sptSet):
		min = dist[0]
		min_index = 0

		for v in range(self.V):
			if (sptSet[v] == False and dist[v] < min):
				min = dist[v]
				min_index = v

		return min_index


	def dijkstra(self, src):
		dist = [maxint]*self.V
		sptSet = [False]*self.V

		dist[src] = 0

		# print(self.graph)

		for count in range(self.V-1):
			u = self.minDistance(dist, sptSet)

			sptSet[u] = True

			for v in range(self.V):
				if (sptSet[v] == False and self.graph[u][v]!=0 and dist[u] != maxint and dist[u] + self.graph[u][v] < dist[v]):
					dist[v] = dist[u] + self.graph[u][v]

		print (self.graph)
		print (dist)


n = int(input())
g = Graph(n)


for i in range(n):
	edge = int(input())
	for t in range(edge):
		t1, t2 = input().split()
		j = int(t1)
		w = int(t2)
		g.graph[i][j] += w
		g.graph[j][i] += w

print(g.graph)		


g.dijkstra(0)