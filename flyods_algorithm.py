class Node:
    def __init__(self, data):
        self.data= data
        self.ref=None
    def detectcycle(head):
        fast=head
        slow=head
        loopexist=0
        while (fast!=None and slow!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
            if fast == slow:
                loopexist=1
                break
        if (loopexist):
            slow=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            return slow
        return None

head=Node('a')
nodeB=Node('b')
nodeC=Node('c')
nodeD=Node('d')
nodeE=Node('e')
nodeF=Node('f')
nodeG=Node('g')
nodeH=Node('h')
nodeI=Node('i')
nodeJ=Node('j')

head.next=nodeB
nodeB.next=nodeC
nodeC.next=nodeD
nodeD.next=nodeE
nodeE.next=nodeF
nodeF.next=nodeG
nodeG.next=nodeH
nodeH.next=nodeI
nodeI.next=nodeJ
nodeJ.next=nodeD

head=Node.detectcycle(head)
print(head.data)