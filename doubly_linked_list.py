class node:
    def __init__(self, data=None, back=None):
        self.data=data
        self.back=back
        self.next=None

class doubly_linked_list:
    def __init__(self):
        self.head=node()

    def append(self, data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
                cur=cur.next
        if self.length()==0:
            new_node.back=None
        else:
            new_node.back=cur
        cur.next=node(data)

    def display(self):
        cur=self.head
        arr=[]
        while cur.next!=None:
                cur=cur.next
                arr.append(cur.data)
        print(arr)
    
    def length(self):
        counter=0
        cur=self.head
        while cur.next!=None:
             counter+=1
             cur=cur.next
        return counter
    def get(self, index):
         if index>self.length():
              print("ERROR. INDEX GREATER THAN LENGTH!") 
              return
         counter=0
         cur=self.head
         while True:
              cur=cur.next
              if index==counter:
                   return cur.data
              counter+=1
    def erase(self, index):
         if index>self.length():
            print("ERROR. INDEX IS GREATER THAN LENGTH!")
            return
         counter=0
         cur=self.head
         while True:
              last_node=cur
              cur=cur.next
              if index==counter:
                   last_node.next=cur.next
                   if cur.next!=None:
                        cur=cur.next
                        cur.back=last_node
              counter+=1
my_list=doubly_linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()


