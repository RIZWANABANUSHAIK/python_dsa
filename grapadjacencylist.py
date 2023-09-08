def add_node(v):
    if v in graph:
        print(v,"is already present")
    else:
        graph[v]=[]
def add_edge(v1,v2)#cost):
    if v1 not in graph:
        print(v1,"is not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        # list1=[v2,cost]
        # list2=[v1,cost]  #for directed this line is not needed
        graph[v1].append(list1)
        graph[v2].append(list2) # for directed this line is not needed
def delete_node(v):
    if v not in graph:
        print(v,"is not in graph")
    # else:
    #     graph.pop(v)
    #     for i in graph:    @ for unweigted undirected graph
    #         list1 = graph[i]
    #         if v in list1:
    #             list1.remove(v)
    # for weigted undirected graph
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v ==j[0]:
                    list1.remove(j)
                    break

def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"not present")
    elif v2 not in graph:
        print(v2,"not present")
    else:
        temp = [v1,cost]
        temp1=[v2,cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)
    

graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_edge("A","B",10)
add_edge("A","C",20)
add_edge("E","G",10)
add_edge("A","F",10)
add_edge("E","B",10)
add_edge("F","B",10)
add_edge("C","B",10)
add_edge("D","B",10)
print(graph)
delete_edge("A","F",10)
print(graph)