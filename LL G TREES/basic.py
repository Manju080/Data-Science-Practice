from opp import Linkedlist


class Node:
    def __init__(self, data=None, next=None,prev=None):
        self.data = data
        self.next = next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
    
    def fprint(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    def bprint(self):
        if self.tail is None:
            print("empty")
            return
        itr=self.tail
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->' if itr.prev else str(itr.data)
            itr=itr.prev
        print(llstr)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def insert_at_begining(self,data):
        node =Node(data,None)
        self.head=None
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=



if __name__=="__main__":
    ll=Linkedlist() 
         
        