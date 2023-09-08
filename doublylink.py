class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
    
class Doublylist:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data ,"---->",end=" ")
                n=n.nref

    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("doubly linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"----->",end=" ")
                n=n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node (data)
            self.head = new_node
        else:
            print("linked list is not empty")
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref = new_node
            new_node.pref = n
    def add_after(self,data,x):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            n=self.head
            while n is not None:
                if x== n.data:
                    break
                n=n.nref

            if n is None :
                print("given node is not present in the data")

            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref =n
                if n.nref is  not None:
                    n.nref.pref = new_node
                n.nref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            n=self.head
            while n is not None:
                if x== n.data:
                    break
                n=n.nref
            if n is None :
                print("given node is not present in the data")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                    n.pref = new_node
    def delete_begin(self):
        if self.head is None :
            print(" dl is empty cant delete")
            return
        if self.head.nref is None:
            self.head = None
            print("after deleting it became empty")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None :
            print(" dl is empty cant delete")
            return
        if self.head.nref is None:
            self.head = None
            print("after deleting the node the dl is empty")
        else:
            n= self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref = None

    def delete_by_value(self,x):
        if self.head is None :
            print(" dl is empty cant delete")
            return
        if self.head.nref is  None:
            if x == self.head.data:
                self.head = None
            else:
                print("value is not there")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n= self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref 
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("given node is not present")



LL1=Doublylist()
LL1.insert_empty(10)
LL1.add_begin(20)
LL1.add_end(50)
LL1.add_after(100,10)
LL1.add_before(200,20)
LL1.delete_begin()
LL1.delete_end()
LL1.delete_end()
# LL1.delete_by_value(100)
LL1.delete_by_value(20)   
LL1.delete_by_value(10)
LL1.print_LL()
# LL1.print_LL_reverse()

