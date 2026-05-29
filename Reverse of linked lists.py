class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp
    '''def reverse(self):
        temp=None
        curr=self.head
        while curr:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        if temp:
            self.head=temp.prev
    def mid(self):
        slow=self.head
        fast=fast.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print("Middle node:",slow.data)
    def search(self,key):
        pos=1
        temp=self.head
        while temp:
            if temp.data==key:
                pos=pos+1
                print(key,"is found at position",pos)
                return
            temp=temp.next
            pos=pos+1
        print(key,"not found")'''
    '''def Palindrome(self):
        left=self.head
        right=self.head
        while right.next:
            right=right.next
        while left!=right and right.next!=left:
            if left.data!=right.data:
                print("It is not a palindrome")
                return
            left=left.next
            right=right.prev
        print("It is a palindrome")
    def rotate(self,k):
        curr=self.head
        count=1
        while count<k and curr:
            curr=curr.next
            count+=1
        if curr is None:
            return
        knode=curr
        while curr.next:
            curr=curr.next
        curr.next=self.head
        self.head.prev=curr
        self.head=knode.next
        self.head.prev=None
        knode.next=None
        print("Rotated")
    def back_traverse(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end="->")
            temp=temp.prev
        print("None")        
    def count(self):
        count=0
        temp=self.head
        while temp:
            temp=temp.next
            count+=1
        print(count)'''
    def traverse(self):
        temp=self.head
        count=0
        while temp:
            print(temp.data,end="->")
            temp=temp.next
            count+=1
        print("None")
        print(count)
d=DLL()
d.insert_end(10)
d.insert_end(20)
d.insert_end(30)
d.insert_end(40)
#d.Palindrome()
#d.rotate(2)
d.traverse()
#d.count()
#d.back_traverse()
#d.reverse()
