from collections import defaultdict

# Read data from the stdin
# Read in the number of vertices (n) and edges (m)

# n vertices
n = int(input())

# m edges
m = int(input())

edges, queries = [], []

for edge in range(m):
    edges.append(input().split())

# Read the number of q
q = int(input())

for query in range(q):
    queries.append(input().split())
	
# Finish reading the data
	
# Print a `1` to stdout for each query. This section should be altered to instead print a `1` where the
# query indicates a connection and `0` else.

# In the following section, run BFS q times.
# Since we have q pairs of edges
# Notice that each BFS takes O(n+m) timw
# So the worst running time should be O(q*(n+m))
# If using the BFS we have already found a path, we stop the algorithm
# The worst case can happen if we traverse the whole graph every for all q BFSs.

# The following is the BFS function
# BFS BFS BFS

def BFS (start , end , n):
	layers = []
	next_layer = [start]
	
	seen = {}
	for num in range(n):
		key = str(num)
		seen[key] = 0
	
	current_layer = [start]
	
	while len(current_layer) != 0:
		layers.append(current_layer)
		for u in current_layer:
			for edge in edges:
				if edge[0] == u:
					if edge[1] == end:
						return True
						# If we have already reach the destination, return true, stop
					
					if seen[edge[1]] == 0:
						next_layer.append(edge[1])
						seen[edge[1]] = 1
				elif edge[1] == u:
					if edge[0] == end:
						return True
						# If we have already reach the destination, return true, stop
					
					if seen[edge[0]] == 0:
						next_layer.append(edge[0])
						seen[edge[0]] = 1
		
		current_layer = next_layer
		next_layer = []
			
	return False





for query in queries:
	start = query[0]
	end = query[1]
	print(int(BFS(start , end , n)))
    #print(int(True))
