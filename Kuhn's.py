
from random import shuffle

FREE = -1 
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


class Matching:
    def __init__(self, n, next_best):
        self.n = n
        self.next_best = next_best
        self.matching = [FREE] * n  
    
    def match(self, agent, visited):
        for house in range(self.n):
            if visited[house]:
                continue
            visited[house] = True
            if self.next_best.query(agent) == house:
                if self.matching[house] == FREE or self.preferred(self.matching[house], agent):
                    self.matching[house] = agent
                    return True
        return False


    def preferred(self, current_agent, new_agent): 
        house = self.next_best.query(new_agent)
        return self.next_best.prefs[new_agent][house] < self.next_best.prefs[current_agent][house]


    def find_matching(self):
                            for agent in range(self.n):
                                 visited = [False] * self.n
                                 self.match(agent, visited)
              

    def print_matching(self):
        for house, agent in enumerate (self.matching):
            print(f'House {house} is matched with Agent {agent}')


    
n = 5  
next_best = NextBest(n)
dfs = DFS(n, next_best)
dfs.find_matching()
dfs.print_matching()


