def add_node(v):
    if v in graph:
        print(v,"is already present")
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def DFS(node,visited,graph):
    if node not in graph:
        print("node is not present")
        return  
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)

visited = set()
graph={}
add_node("a")
add_node("b")
add_node("c")
add_node("d")
add_node("e")
add_edge("a","b")
add_edge("b","e")
add_edge("a","c")
add_edge("b","d")
add_edge("c","d")
add_edge("e","d")
DFS("A",visited,graph)