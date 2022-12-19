
class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class slinkedlist:
    def __init__(self,data):
        self.head=node(data)

sdata1=slinkedlist(10)
sdata2=slinkedlist(20)
sdata3=slinkedlist(30)
sdata4=slinkedlist(40)

sdata1.head.next=sdata2
sdata2.head.next=sdata3
sdata3.head.next=sdata4

targetnode=sdata1

while (targetnode.head.next!=None):
    print(targetnode.head.data)
    targetnode=targetnode.head.next