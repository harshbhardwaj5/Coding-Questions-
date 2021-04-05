from queue import Queue          
adj={"A":["B","C"],"B":["A","C"],"C":[]} 
visited={}
ls=[]
for i in adj.keys():
    visited[i]=False 
queue=Queue()
s="A"
queue.put(s)
visited[s]=True
while not queue.empty():
    u=queue.get() 
    ls.append(u)

    for v in adj[u]:
        if not visited[v]:
            visited[v]=True 
            queue.put(v)
print(ls)