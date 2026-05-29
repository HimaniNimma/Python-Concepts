#Linked lists
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
temp=n1
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("None")
#Single linked list
class  Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    #Insert a new node in the begining of the list
    def insert_begin(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        new.next=self.head
        self.head=new
    #Insert a new node in the middle of the list
    def insert_middle(self,pos,data):
        new=Node(data)
        temp=self.head
        for i in range(pos-2):
            temp=temp.next
        new.next=temp.next
        temp.next=new
    #Insert a new node in the ending of the list
    def insert_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    #Delete a new node in the begining of the list
    def del_begin(self):
        if self.head is None:
            print("List is Empty")
            return
        self.head=self.head.next
    #Delete a new node in the begining of the list
    def del_end(self):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    #Delete a new node in the begining of the list
    def del_middle(self,middle):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        for i in range(middle-2):
            temp=temp.next
        temp.next=temp.next.next
    #Search a node in the linked list
    def search(self,key):
        temp=self.head
        pos=1
        while temp:
            if temp.data==key:
                print(key,"is found at ",pos)
                return
            temp=temp.next
            pos=pos+1
        print("Element found")
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
s=SLL()
s.insert_begin(30)
s.insert_begin(29)
s.insert_begin(28)
s.insert_middle(3,40)
s.insert_middle(5,60)
s.insert_end(31)
s.insert_end(32)
s.del_begin()
s.del_end()
s.del_middle(2)
s.traverse()
s.search(60)
