
import copy

FREE = -1  

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
        
        for i in range (0,len(path),2):
            matching [path[i]] = path[i+1]
        return matching

        """
        new_matching = matching[:]  # Create a copy of matching
        for i in range(0, len(path), 2):
             new_matching[path[i]] = path[i + 1]
             return new_matching
        

    def is_adjacent(self, agent, house, graph):
         return house in self.graph[agent]
         
    def maxmatching(self):
            unreachable_house = []
            unreachable_agent = []
            even_house = [] 
            even_agent = []
            odd_house = []
            odd_agent = [] 
            diff_list = []
            for i in range(self.n):
                 even_agent.append(i) 
                 even_house.append(i)
            for i in range(self.n):
                 if self.matching[i] == -1:
                    if (self.hasAugmenting(i, self.matching, self.graph) == []):
                        if (i == (self.n)-1):
                            return self.matching
                    else:
                         x = self.hasAugmenting(i, self.matching, self.graph)
                         temp = self.matching
                         #print(temp)
                         self.matching = self.flipPath(x, temp)                              
                         #print(self.matching)
                         for index, (elem1, elem2) in enumerate(zip(temp, self.matching)):
                            if elem1 != elem2:
                                diff_list.append(index)
                                last_index = diff_list[-1]
                                differ_matching = self.matching[last_index] 
                                even_house.remove(differ_matching)
                                even_agent.remove(last_index)
                                
                                if self.is_adjacent(last_index, differ_matching, self.graph):
                                    if any(differ_matching in self.graph[i] for i in even_agent):
                                        odd_house.append(differ_matching)
                                        even_agent.append(last_index)
                                    elif any(i in even_house for i in self.graph[last_index]):
                                        odd_agent.append(last_index)
                                        even_house.append(differ_matching)
                                    else:
                                        unreachable_agent.append(last_index)
                                        unreachable_house.append(differ_matching)

            return self.matching, even_agent, even_house, odd_agent, odd_house, unreachable_agent, unreachable_house
    

                        
    def addEdgesAndMatch(E):
        pass


#Test Cases: 
    
graph1 = {  0 : [1],
            1 : [1],
            2 : [],
            3 : [2, 3],
            4 : [4]}

matching_instance = Matching([-1,-1,-1,-1, -1],5, graph1)
#print(matching_instance.flipPath([0,0,1,1,2,2,3,3], [-1, 0, 1, 2] ) )
#print(matching_instance.hasAugmenting(3, [1, 2, 3, -1],graph1))
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

list1 = [0, -1, -1, -1]
list2 = [0, 1, -1, -1]

differences = []

for index, (elem1, elem2) in enumerate(zip(list1, list2)):
    if elem1 != elem2:
        differences.append((index, elem1, elem2))

#print("Differences found at:")
#for diff in differences:
#    print(f"Index: {diff[0]}, Value in list1: {diff[1]}, Value in list2: {diff[2]}")
