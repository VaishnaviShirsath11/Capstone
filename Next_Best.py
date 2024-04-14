import Matching as match 
from random import shuffle

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
  
# Initialize a NextBest instance with 4 agents
nb = NextBest(4)

# Query the preferences of each agent
for agent in range(nb.n):
    print(f"Agent {agent} preferences:", nb.prefs[agent])

# Suppose we query the preferences for each agent sequentially
for agent in range(nb.n):
    print(f"Querying preferences for Agent {agent}:")
    for _ in range(nb.n):
        print("Query result:", nb.query(agent))

# Print the number of queries made
print("Total queries made:", nb.qcount)
