class node:
    def __init__(self,data):
        self.data=data 
        self.visited=False
        self.adjlist=[];

def dfs(n):
    n.visited=True
    print(n.data)
    for i in n.adjlist:
        if i.visited!=True:
            dfs(i)


node1=node(1)
node2=node(4)
node3=node(3)

node1.adjlist.append(node2)

node1.adjlist.append(node3)
dfs(node1)



        

