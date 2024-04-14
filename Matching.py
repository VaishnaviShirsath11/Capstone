
from queue import Queue
from random import shuffle

FREE = -1  

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
    def __init__(self, matching, n, graph):
        self.matching = matching
        self.n = n
        self.graph = graph

    def hasAugmenting(self, start, matching, graph):
        def augmenting_path(agent): 
            #print(agent)
            if visited_agent[agent] == False:    
                visited_agent[agent] = True
                #print(visited_agent)
                #start is a free vertex  
                for house in graph[agent]: 
                        if not visited_house[house]: 
                            #print(house)
                            visited_house[house] = True
                            #print(visited_house)
                            previous[house] = agent
                            #print(previous)
                            if house not in matching:
                                return house
                            else:
                                new_agent = matching.index(house)
                                result = augmenting_path(new_agent) 
                                if result != None:
                                    return result  #if last vertex found return it, else continue the function 
                        
            return None 
        
        def getaugmenting(previous, house, matching, start):
            path = [-1]
            while path[-1] != start:
                        path.extend([house, previous[house]])
                        house = matching[previous[house]]
            return list(path[1:].__reversed__())
    
          
        visited_agent = [False] * self.n
        visited_house = [False] * self.n
        previous = [FREE] * self.n 
        house = augmenting_path(start)
        if house is None: 
             return [] 
        else:
            return getaugmenting(previous, house, matching, start) 
    
        
    def flipPath(self, path, matching):
        """
        Input: path - list of vertices, which represents an augmenting path
        output: updates matching by flippping edges on augmenting path provided as input
        """
        new_matching = matching[:]  # Create a copy of matching
        for i in range(0, len(path), 2):
             new_matching[path[i]] = path[i + 1]
        return new_matching
        
      
    def maxmatching(self):
                for i in range(self.n):
                    if self.matching[i] == -1:
                        if (self.hasAugmenting(i, self.matching, self.graph) == []):
                            if (i == (self.n)-1):
                                return self.matching   
                        else:
                            x = self.hasAugmenting(i, self.matching, self.graph)   
                            temp = self.matching    
                            print(temp)
                            self.matching = self.flipPath(x, temp)                              
                            print(self.matching)   
                return self.matching
        

    def decompose(self, matching, graph):
        even_house = [i for i in range(self.n) if i not in matching]
        even_agent = [i for i in range(self.n) if matching[i] == -1]
        odd_house = []
        odd_agent = []

        def decompose_agent(agent):
            for neighbour in graph[agent]:
                if neighbour not in odd_house:
                    odd_house.append(neighbour)
                    if neighbour in matching:
                         x = matching.index(neighbour)
                         even_agent.append(x)
                         decompose_agent(x)           

        def decompose_house(house):
            for i in range(self.n):
                if house in graph[i] and i not in odd_agent:
                    odd_agent.append(i)
                    x = matching[i]
                    even_house.append(x)
                    decompose_house(x)

        for i in even_agent:
            decompose_agent(i)

        for i in even_house:
            decompose_house(i)

        unreachable_agent = [i for i in range(self.n) if i not in even_agent and i not in odd_agent]
        unreachable_house = [i for i in range(self.n) if i not in even_house and i not in odd_house]

        return even_house, even_agent, unreachable_agent, unreachable_house, odd_agent, odd_house         


    def NextBestMatch(agents, houses):
        unfinished_agents = list(range(agents))
        available_house = list(range(houses))
        graph = {i: [] for i in range(agents)}
        matching = [-1 for _ in range(agents)]
        maximum_matching = [-1 for _ in range(agents)]
        forbidden_pairs = {i: [] for i in range(agents)}
        x = NextBest(agents)
        count = 0 

        if agents == 2:
            a1 = unfinished_agents[0]
            h1 = x.query(a1)
            available_house.remove(h1)
            h2 = available_house[0]
            maximum_matching.extend([h1, h2])
            maximum_matching.pop(0)
            maximum_matching.pop(0)
            return maximum_matching

        for i in range(agents):
            for a in unfinished_agents:          
                h = x.query(a)  
                #print(h)        
                if h in available_house and h not in forbidden_pairs[a]:  
                    graph[a].append(h)
            #print(graph)

            matching_instance = Matching(matching, agents, graph)
            maximum_matching = matching_instance.maxmatching()
            #print(maximum_matching)
            decomposition = matching_instance.decompose(maximum_matching, graph)
            #print(decomposition)

            for agent in range(agents):
                if agent in decomposition[2] or agent in decomposition[4]:
                    if agent in unfinished_agents:
                        unfinished_agents.remove(agent)
                    #print(unfinished_agents)
                    for neighbor in range(agents): 
                        if neighbor > count and len(graph[agent]) > neighbor:  
                            graph[agent].pop(neighbor)
                            #print(graph)


            for house in range(houses):
                if house in decomposition[3] or house in decomposition[5]:
                    if house in available_house:
                        available_house.remove(house)
                    #print(available_house)
                    for agent, neighbors in graph.items():
                        if house in neighbors and graph[agent].index(house) > count:  # Remove edges with rank greater than 'count'
                            graph[agent].remove(house)
                            #print(graph)

            for i in range(agents):
                for j in graph[i]:
                    if (j in decomposition[5] and i in decomposition[4]) or \
                    (j in decomposition[3] and i in decomposition[4]) or \
                    (j in decomposition[5] and i in decomposition[2]):
                        forbidden_pairs[i].append(j)
                        #print(forbidden_pairs)
                        graph[i].remove(j)
                        #print(graph)
            
            count = count + 1 
    
        return maximum_matching 



#Test Cases: 
    
graph = {  0 : [0, 1, 2, 3],
            1 : [0, 2, 1, 3],
            2 : [0, 1, 3, 2],
            3 : [1, 2, 0, 3]}

matching_instance = Matching([-1,-1, -1, -1],4, graph)
#print(matching_instance.flipPath([1, 0, 0, 1], [0, -1, -1, -1] ) )
#print(matching_instance.hasAugmenting(1, [0, -1, -1, -1],graph))
#print(matching_instance.maxmatching())
#print(matching_instance.decompose([0, 2, 3, 1], graph))
#print(Matching.NextBestMatch(10, 10))

