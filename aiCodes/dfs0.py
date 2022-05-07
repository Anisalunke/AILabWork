# DFS Algorithm

# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }

graph = {
    '0' : ['1','2','3'],
    '1' : [],
    '2' : ['4'],
    '3' : [],
    '4' : []
}

visited = [] # List for visited nodes.
stack = []     # Initialize a queue
source_node = '0' # Source node

def dfs(visited, graph, node): #function for BFS
  visited.append(node)
  stack.append(node)

  while stack:     # Creating loop to visit each node
    m = stack.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.insert(0,neighbour)
        stack.insert(0,neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, source_node)    # Call the function