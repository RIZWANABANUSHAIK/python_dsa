class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):            # this having no mistake but it doent giving output 
        self.head=None              # showing that tempcoderunner.file so dont panic riz

    def print_LL(self):
        if self.head is None:
            print("linked list is empty")

        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node         

LL1=linkedlist()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.add_begin(50)
LL1.print_LL()