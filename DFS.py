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