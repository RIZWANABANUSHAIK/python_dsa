class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return 
        if self.key >data :
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("node is find")
            return
        if data<self.key :
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present")

    def pre_order(self):
        print(self.key)
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key)
        if self.rchild:
            self.rchild.in_order()
    
    def post_order(self):
        if self.lchild:
            self.lchild.in_order()
        if self.rchild:
            self.rchild.in_order()
        print(self.key)

    def delete(self,data,curr):
        if self.key is None:
            print("tree is empty")
            return
        if self.key>data:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
              print("given node is not present")
        elif self.key<data:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("node is not present")
        else:
            if self.lchild is  None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return 
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return 
                self = None
                return temp
            node = self.rchild
            while node.lchild :
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("smallest is",current.key)
    def max_node(self):
        current = self
        current = self
        while current.rchild:
            current = current.rchild
        print("largest is",current.key)

def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
root =  BST(10)
# root.insert(10)
list =[6,3]
for i in list:
    root.insert(i)
# root.search(15)
# print("preorder")
# root.pre_order()
# print("inorder")
# root.in_order()
# print("postorder")
# root.post_order()
# if count(root)>1:
#     root.delete(10,root.key)
# else:
#     print("cant perform the deletion operation")

# print("after deleting")
# root.pre_order()
# print(count(root))
root.max_node()
root.min_node()