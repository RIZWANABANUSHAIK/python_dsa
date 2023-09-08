# for unweighted,undirected graph
# adjacencymatrix
def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present")
    else:
        node_count= node_count+1
        nodes.append(v)
        for n in graphs:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graphs.append(temp)
# for weigted graph
#def add_edge(v1,v2,cost)
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present")
    elif v2 not in nodes :
        print(v2,"not present")
    else:
        index1 = nodes.index(v1)
        index2= nodes.index(v2)
        #for weigted graph
        # graphs [index1][index2] = cost
        # graphs [index2][index1] = cost
        graphs [index1][index2] = 1
        graphs [index2][index1] = 1 # for directed graph this is not needed

def del_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not present")
    else:
        index1= nodes.index(v)
        node_count=node_count-1
        nodes.remove(v)
        graphs.pop(index1)
        for i in graphs:
            i.pop(index1)
def del_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"not in nodes")
    elif v2 not in nodes:
        print(v2,"is not in nodes")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graphs[index1][index2]=0
        graphs[index2][index1]=0

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graphs[i][j],"<3"),end = " ")
        print()
nodes = []
graphs= []
node_count = 0
# print("before adding")
# print(nodes)
# print(graphs)
add_node("A")
add_node("B")
add_node("C")
# for weighted graph
# add_edge("A","B",34)
# add_edge("A","C",35)
add_edge("A","B")
add_edge("A","C")
# print("after adding")
# print(nodes)
# print(graphs)
print_graph()
del_edge("A","C")
print("after deleting")
print_graph()
# print("afterdeleting")
# del_node("B")
print(nodes)
print(node_count)
