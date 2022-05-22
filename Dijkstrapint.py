#Dijkstra's Algorithm, but with printing
#All of the code for setting up the graph, and the algorithm itself, comes from chapter 6 of Grokking Algorithms by Aditya Bhargava
#The printing function is my own work (with help from stack overflow of course ^_^)

graph = {}
#weighted graph
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph ["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

#table of lowest cost to reach each node
infinity = float("inf") # must be impossible to choose a node without an accessible edge
costs = {}
costs["start"] = 0
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#parents hash
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
processed = [] #make sure we dont recalculate nodes over and over

def dijkstra(graph, costs, parents):
  node = findCheapest(costs) #find cheapest node not yet processed
  while node is not None: #while we have nodes to process
    cost = costs[node] #take the node found
    neighbors = graph[node]
    for n in neighbors.keys(): #look at neighbors of the node
      new_cost = cost + neighbors[n] #check cost of path
      if costs[n] > new_cost: #if we've found a cheaper path
        costs[n] = new_cost #update that to be our new cost
        parents[n] = node #and our new best-guess path
    processed.append(node)
    node = findCheapest(costs) #add to processed and loop
  printPath(parents, costs, "start", "fin")

def findCheapest(costs):
  lowest_cost = float("inf")
  lowest_cost_node = None
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node

def printPath(path, costs, start, end): #takes dijkstra parents, costs, start node name, and end node names as input
  pathList = [start]
  step = start
  switchPath = {y: x for x, y in path.items()} #need to switch keys and values around. from https://stackoverflow.com/questions/8305518/switching-keys-and-values-in-a-dictionary-in-python
  finalPath = {}
  while end not in pathList: #"walks" through the path until it finds the end
    nextStep = switchPath[step]
    pathList.append(nextStep)
    step = nextStep
  for i in pathList:
    finalPath[i] = costs[i] #creates a dict with path as keys and costs as values, this time in the correct order
  result = "".join(str(key) + "(" + str(value) + ") -> " for key, value in finalPath.items()) #pretty dictionary string code from https://stackoverflow.com/questions/39578141/python-how-to-print-dictionary-in-one-line
  print(result.rstrip(" ->")) #clean up and print
  

dijkstra(graph, costs, parents)
