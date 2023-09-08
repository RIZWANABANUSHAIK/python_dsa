nodes =[]
node_count = 0
graph =[]
def del_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not present")
    else:
        index1= nodes.index(v)
        node_count=node_count-1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

