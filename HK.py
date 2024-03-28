
from random import shuffle
from queue import Queue


INF = 2147483647
NIL = 0

class NextBest:
  def __init__(self, n):
    self.n = n
    self.qcount = 0
    self.prefs = [list(range(n)) for _ in range(n)]
    for p in self.prefs:
        shuffle(p)
    self.next = [0 for _ in range(n)]

  def query(self, agent):
    self.qcount += 1
    nextId = self.next[agent]
    assert (nextId < self.n)
    self.next[agent] += 1
    return self.prefs[agent][nextId]
  
class Agent_Preference:
    def __init__(self, i, r):
        self.agent_index = i 
        self.pref_list = r

    def getagent(self): 
        return self.agent_index
    
    def getpreflist(self): 
        return self.pref_list
   


class BipartiteGraph():
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.neighbour = [[] for _ in range(m + 1)]
        self.matched_vertices = {}

    def add_edge(self, v1, v2):
        self.neighbour[v1].append(v2)

    def bfs(self):
        Q = Queue()
        for v1 in range(1, self.m + 1):
            if self.pairV1[v1] == NIL:
                self.dist[v1] = 0
                # v1 is a free vertex, add it to the queue
                Q.put(v1)
            else:
                self.dist[v1] = INF
        self.dist[NIL] = INF
        while not Q.empty():
            v1 = Q.get()
            if self.dist[v1] < self.dist[NIL]:
                for v2 in self.neighbour[v1]:
                    if self.dist[self.pairV2[v2]] == INF:
                        self.dist[self.pairV2[v2]] = self.dist[v1] + 1
                        Q.put(self.pairV2[v2])
        return self.dist[NIL] != INF

    def dfs(self, v1):
        if v1 != NIL:
            for v2 in self.neighbour[v1]:
                if self.dist[self.pairV2[v2]] == self.dist[v1] + 1:
                    if self.dfs(self.pairV2[v2]):
                        self.pairV2[v2] = v1
                        self.pairV1[v1] = v2
                        return True
            self.dist[v1] = INF
            return False
        return True

    def hopcroftKarp(self):
        self.pairV1 = [0 for _ in range(self.m + 1)]
        self.pairV2 = [0 for _ in range(self.n + 1)]
        self.dist = [0 for _ in range(self.m + 1)]
        result = 0

        while self.bfs():
            for agent in range(1, self.m + 1):
                for v1 in range(1, self.m + 1):
                    if self.pairV1[v1] == NIL and self.dfs(v1):
                        result += 1

        for v1 in range(1, self.m + 1):
            if self.pairV1[v1] != NIL:
                self.matched_vertices[v1] = self.pairV1[v1]

                # Return matched and unmatched vertices
                matched = {v1: self.pairV1[v1] for v1 in range(1, self.m + 1) if self.pairV1[v1] != NIL}
                unmatched = [v1 for v1 in range(1, self.m + 1) if self.pairV1[v1] == NIL]

                even_vertices = []
                odd_vertices = []
                unreachable_vertices = []

                for v1 in range(1, self.m + 1):
                    if self.dist[v1] == INF:
                        unreachable_vertices.append(v1)
                    elif self.dist[v1] % 2 == 0:
                        even_vertices.append(v1)
                    else:
                        odd_vertices.append(v1)

                return result, self.matched_vertices, even_vertices, odd_vertices, unreachable_vertices
            
        
        





g = BipartiteGraph(5, 5)
g.add_edge(1, 1)
g.add_edge(2, 2)
g.add_edge(2, 3)
g.add_edge(4, 3)
g.add_edge(5, 3)
g.add_edge(5, 5)
print(g.hopcroftKarp())

# Create an instance of NextBest
nbb = NextBest(5)
# Access and print attributes
print("Value of n:", nbb.n)
print("Number of queries:", nbb.qcount)
# Test query method
print("Query result for agent 0:", nbb.query(0))
print("Query result for agent 0:", nbb.query(0))
print("Query result for agent 0:", nbb.query(0))
print("Query result for agent 0:", nbb.query(0))
print("Query result for agent 0:", nbb.query(0))

print("Query result for agent 1:", nbb.query(1))

print("Number of queries:", nbb.qcount)


# Print preference lists
print("Preference lists:")
input_array = []

for i, pref_list in enumerate(nbb.prefs):
    input_array.append(Agent_Preference(i, pref_list))

#rint(input_array)

for i in range (len(input_array)):
    print(input_array[i].getagent(), input_array[i].getpreflist())

# Perform assertions or checks
assert nbb.n == len(nbb.prefs) == len(nbb.next), "Length mismatch"



def modify_matching(path, matching):
    path = [] 
    matching = ()




#path = []
#matching = []