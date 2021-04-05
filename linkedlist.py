class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 

class linkedlist:
    def __init__(self):
        self.head=None 
    def printll(self):
        if self.head==None:
            print("empty linked list")

        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next 

    def addbeg(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode

    def looplinkedlist(self):
        slow=self.head
        fast=self.head
        while(slow and fast and fast.next):
            slow=slow.next 
            fast=fast.next.next 
            if slow==fast:
                print("loop found ")
                return
        return 
node(30)
n=linkedlist()
n.addbeg(20)
n.addbeg(30)
n.head.next.next = n.head
n.looplinkedlist()

