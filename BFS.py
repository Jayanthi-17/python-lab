graph={
    'A':['B','C','D'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','A','C','E'],
    'E':['C','D']
}
visitednodes=[]
queuenodes=[]
def BFS(visitednodes,graph,snode):
    visitednodes.append(snode)
    queuenodes.append(snode)
    print()
    while queuenodes:
       m=queuenodes.pop(0)
       print(m,end=" ")
       for neighbor in graph[m]:
           if neighbor not in visitednodes:
               visitednodes.append(neighbor)
               queuenodes.append(neighbor)

snode=input("Enter the starting node(A,B,C,D,E): ".upper())
BFS(visitednodes,graph,"A")
           