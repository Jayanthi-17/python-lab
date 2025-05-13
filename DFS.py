'''
🔶 Depth-First Search (DFS)
📘 Definition:
DFS explores as deep as possible along a path before backtracking.
It uses recursion or a stack (LIFO) to track the path.

🔧 How It Works:
Start from a node.

Visit it, go to its first unvisited neighbor.

Continue down the path until no more unvisited neighbors, then backtrack.
'''
graph={
    'A':['B','C','D'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','A','C','E'],
    'E':['C','D']
}
visitedNodes=list()
def dfs(visitedNodes,graph,node):
    if node not in visitedNodes:
        print(node,end=" ")
        visitedNodes.append(node)
        for neighbor in graph[node]:
            dfs(visitedNodes,graph,neighbor)

snode=input("Enter the starting node(A,B,C,D,E): ").upper()
dfs(visitedNodes,graph,snode)