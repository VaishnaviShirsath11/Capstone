
FREE = -1  

class Matching:
    def __init__(self, matching, n, graph):
        self.matching = matching
        self.n = n
        self.graph = graph

    def hasAugmenting(self, start, matching, graph):
        def augmenting_path(agent): 
            if visited_agent[agent] == False:
                visited_agent[agent] = True
                #start is a free vertex 
                for house in graph[agent]:
                        if not visited_house[house]:
                            visited_house[house] = True
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
        #print(house)
        if house is None: 
             return [] 
        else:
            return getaugmenting(previous, house, matching, start) 
    
        

    # def recallDFS(v, N, visited, prev):
    #     visited[v] = True
    #     for u in N[v]:
    #         if not visited[u]:
    #             prev[u] = v
    #             recallDFS(u, N, visited)

        
    def flipPath(self, path, matching):
        """
        Input: path - list of vertices, which represents an augmenting path
        output: updates matching by flippping edges on augmenting path provided as input
        """
        for i in range (0,len(path),2):
            matching [path[i]] = path[i+1]
        return matching

    def maxmatching(self):
            for i in range(self.n):
                 if self.matching[i] == -1:
                    if (self.hasAugmenting(i, self.matching, self.graph) == []):
                        if (i == self.n-1):
                            return self.matching
                    else:
                         x = self.hasAugmenting(i, self.matching, self.graph)
                         temp = self.matching
                         self.matching = self.flipPath(x, temp)
            return self.matching 
    
    def decompose(self, matching):
            unreachable_house = []
            unreachable_agent = []
            even_house = [] 
            even_agent = []
            odd_house = []
            odd_agent = []  
            for i in range(self.n): 
                unreachable_house.append(i)
                unreachable_agent.append(i)  
            if -1 not in matching: 
                    return unreachable_house, unreachable_agent, odd_house, odd_agent, even_house, even_agent 
            else: 
                     x = matching.index(-1)
                     even_agent.append(x)
                     unreachable_agent.remove(x)
                     for i in self.graph[x]:
                          odd_house.append(i)
                          unreachable_house.remove(i)
                          for i in odd_house: 
                               y = matching.index(i)
                               even_agent.append(y)
                               unreachable_agent.remove(y)
                     for i in unreachable_house:
                          if i not in matching:
                               even_house.append(i)
                               unreachable_house.remove(i)
                               for j in range(self.n): 
                                    if i in self.graph[j]:
                                         odd_agent.append(j)
                                         unreachable_agent.remove(j)
                                         z = matching[j]
                                         even_house.append(z)
                                         unreachable_house.remove(z)
            return unreachable_house, unreachable_agent, odd_house, odd_agent, even_house, even_agent
                        
    def addEdgesAndMatch(E):
        pass


#Test Cases: 
    
graph1 = {  0 : [0],
            1 : [0,1],
            2 : [1, 2],
            3 : [2,3]}

matching_instance = Matching([-1,-1,-1,-1],4, graph1)
#print(matching_instance.flipPath([0,0,1,1,2,2,3,3], [-1, 0, 1, 2] ) )
#print(matching_instance.hasAugmenting(3, [1, -1, -1, -1],graph1))
print(matching_instance.maxmatching())
#print(matching_instance.decompose([1, -1, 2, 3, 5, -1]))

"""
def hasAugmenting_helper(self, start, matching, graph): 
        path = [] 
        if matching[start] == FREE:
            while self.visited[start] == False:
                if graph[start] != []:
                    for i in graph[start]:
                        self.visited[start] = True
                        print(self.visited)
                        if i not in matching: 
                            path.append(start)
                            path.append(i)
                            return path
                        else: 
                            x = matching.index(i)
                            if x == start:
                                path.append(i)
                                continue
                            else:
                                path.append(start)
                                #path.append(i)
                                start = x
                            break
                else: 
                    return [] 
        else:
            return []
        return [] 

        


        def getaugmenting(self, previous, house, matching, start):
            path = [] 
            result = -1
            if start == previous[house]: 
                return path
            else: 
                while result != start: 
                        result = matching [previous [house]]
                        path.extend([house, previous[house]])
                        house = result
            return path
"""
