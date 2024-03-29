
FREE = -1  

def finalmatching3(m1):
            start_ind = m1.matching.index(-1)
            if (m1.hasAugmenting(start_ind, m1.matching ,m1.graph) == []):
                return m1.matching 
            else:
                if m1.matching[start_ind] == -1: 
                    x = m1.hasAugmenting(start_ind, m1.matching, m1.graph)
                    temp = m1.matching
                    m1.matching = m1.flipPath(x, temp)
                    k = Matching(m1.matching, m1.n, m1.graph)
                    return finalmatching3(k)

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

    def finalmatching2(self,start_ind):
         if (self.hasAugmenting(start_ind,self.matching, self.graph) == []):
              return self.matching  


    def finalmatching(self,start_ind,matching, graph):
        if (self.hasAugmenting(start_ind,self.matching, graph) == []):
            return self.matching
        else:
            if self.matching[start_ind] == -1:
                    #print(self.hasAugmenting(start_ind,matching,graph))
                    x = self.hasAugmenting(start_ind, matching,graph)
                    print(x)
                    temp = self.matching
                    print(temp)
                    self.matching = self.flipPath(x, temp)
                    print(self.hasAugmenting(start_ind,self.matching,self.graph))
                    return self.finalmatching(self.matching.index(-1),self.matching,self.graph)
             
    
    def maxmatching(self):
            for i in range(self.n):
                 if self.matching[i] == -1:
                    if (self.hasAugmenting(i, self.matching, self.graph) == []):
                        if (i == self.n):
                            return self.matching
                    else:
                         x = self.hasAugmenting(i, self.matching, self.graph)
                         #print(x)
                         temp = self.matching
                         #print(temp)
                         self.matching = self.flipPath(x, temp)
                         #print(self.matching)
            return self.matching 
            
                      
          
        
                 
                 

    



    
            

                
                  
                 
                 
            
            """
            for i in range(self.n):
                if matching[i] == -1: 
                    x = self.hasAugmenting(i, matching, graph)
                    new_matching = self.flipPath(x, matching)
                    
            """
       
    def addEdgesAndMatch(E):
        pass


#Test Cases: 
    
graph1 = {  0 : [1],
            1 : [],
            2 : [2],
            3 : [3]}

matching_instance = Matching([-1,-1,-1,-1],4, graph1)
#print(matching_instance.flipPath([0,0,1,1,2,2,3,3], [-1, 0, 1, 2] ) )
#print(matching_instance.hasAugmenting(3, [1, -1, -1, -1],graph1))
#new_match = finalmatching3(matching_instance)
#print(new_match)
#print(matching_instance.finalmatching(0,matching_instance.matching,matching_instance.graph))
print(matching_instance.maxmatching())


#print(matching_instance.getaugmenting([0,1,2,3], 3, [-1, 0, 1, 2], 0))


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
