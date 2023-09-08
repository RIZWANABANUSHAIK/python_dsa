class Node:
    def __init__(self, data):
        self.data= data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head =None
    
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")

        else:
            n=self.head
            while n is not None:
                print(n.data,"<-----",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node 

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None :
                n = n.ref
            n.ref = new_node

    def reverselist(list):
        previous = None
        n=list.head
        following = n.ref
        while n:
            n.ref = previous
            previous = n
            n= following
            if following:
                following = following.ref
        list.head = previous

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head is None :
            print("linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return 
        n= self.head
        while n.ref is not None:
            if n.ref.data == x :
                break
            n=n.ref
        if n.ref is None :
            print("node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list is not empty")

    def delete_begin(self):
        if self.head is None:
            print("linked list is empty")
            return
        else:
            self.head = self.head.ref
    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("cant delete")
            return
        if x==self.head.data:
            self.head = self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("node is not present")
        else:
            n.ref=n.ref.ref


LL1 = Linkedlist()
# LL1.add_begin(20)
LL1.add_end(90)
LL1.add_end(100)
LL1.add_end(110)
# LL1.add_begin(50)
# LL1.add_after(40,90)
# LL1.add_before(50,20)
# LL1.add_end(30)
# LL1.delete_begin()
# LL1.delete_end()
# LL1.delete_by_value(50)
LL1.print_LL()
LL1.reverselist()
print("\n")
LL1.print_LL()