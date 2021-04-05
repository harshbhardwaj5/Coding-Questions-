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
    

    def addend(self,data):
        newnode=node(data)

        if self.head==None:
            self.head=newnode 
        else:
            n=self.head
            while n.next!=None:   #this is imp n.next not ( n )
                n=n.next 
            n.next=newnode 
    
    def addmiddle(self,data,x):
        n=self.head 
        while n.data!=x  :
            n=n.next 
        newnode=node(data)
        newnode.next=n.next 
        n.next=newnode


    def looplinkedlist(self):
        slow=self.head
        fast=self.head
        while(slow and fast and fast.next):
            slow=slow.next 
            fast=fast.next.next 
            if slow==fast:
                print("loop found ")
                return
        return False

    def reversell(self):
        curr=self.head
        prev=None
        while curr!=None:
            nex=curr.next
            curr.next=prev 
            prev=curr 
            curr=nex
        self.head=prev 

    def lllenght(self):                 #go till last node and add values 
        n=self.head 
        c=0
        while n!=None:
            c+=1 
            n=n.next
        return c

    def lldeleteend(self):
        n=self.head 
        while n.next!=None:
            if n.next.next==None:
                n.next=None
            else:
                n=n.next 
                
            
    def isPalindrome(self):
        fast = slow = self.head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        n=self.head
        while node: # while node and head:
            if node.data != n.data:
                return False
            node = node.next
            n = n.next
        return True


   

n=linkedlist()
n.addbeg(20)
n.addbeg(30)
#n.head.next.next = n.head
n.addend(2)
n.reversell()
n.printll()
if n.looplinkedlist()==False:
    print("Not Found")
#print(n.lllenght())