
#####################
######Algorithm######
#####################

def BFS(G, goal_vertex):
	Q = [] #queue
	root = V[0]
	Q.append(root)
	visited = [] #list of visted vertices
	visited.append(root)

	while len(Q)!=0:
		u = Q.pop()

		if u == goal_vertex:
			print('Goal vertex was found!')
			return u

		for v in E[u]:
			if v not in visited:
				visited.append(v)
				Q.append(v)
	print('Goal vertex was NOT found :(')
	return -1 #return -1 if goal vertex wasn't found

#####################
#######Example#######
#####################

V = [1,2,3,4]
E = {1:{2,4}, 2:{1,3}, 3:{2,4}, 4:{1,3}}
G = (V,E)

BFS(G,4)
BFS(G,5)
BFS(G,1)
