def mindistance(V,dist,visited):
    min=9999
    for v in range(V):
        if dist[v]<min and visited[v]==False :
            min=dist[v]
            min_index = v
    return min_index
def dijkstra(graph,V,src):
    dist=[9999]*V
    dist[src]=0
    visited=[False]*V
    for count in range(V):
        u=mindistance(V,dist,visited)
        visited[u]=True
        for v in range(V):
            if (graph[u][v] >0 and visited[v]==False and dist[v]>dist[u]+graph[u][v]):
                dist[v]=dist[u]+graph[u][v]

    print("vertex \t distance from source")
    for node in range(V):
        print(node , "\t\t",dist[node])


n=int(input("enter number of vertices:"))
print("enter the adjacent matrix:")
g=[]
for i in range(n):
    data=list(map(int,input().split(" ")))
    g.append(data)
s=int(input("enter the source vertex:"))
dijkstra(g,n,s)

