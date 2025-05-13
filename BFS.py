'''
Breadth-First Search (BFS)
📘 Definition:
BFS explores all the nodes level by level (breadth-wise) starting from a given node.
It uses a queue (FIFO) to keep track of nodes to visit.

🔧 How It Works:
Start from a node.

Visit it and add all its neighbors to a queue.

Dequeue one node at a time and repeat the process.
'''

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
           