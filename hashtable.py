class node: 
    def __init__(self, data=None):# use linked lists to handle collisions
        self.data=data
        self.next=None
class hashtable:
    def __init__(self, numval):
        self.arr=[node() for i in range(numval)]
        self.length=numval
    #simple ascii hash function
    def hash_func(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h% self.length
    #use dunder method so we can add and access methods like we would a typical python dictionary
    def __setitem__(self, key, value):
        found=False
        index=self.hash_func(key)
        cur=self.arr[index]
        while cur.next != None:
            cur=cur.next
            if cur.data[0]==key:
                found=True
                cur.data[1]=value
        if not found:
            new_node=node((key,value))
            cur.next=new_node
        
    def __getitem__(self, key):
        found=False
        index=self.hash_func(key)
        cur=self.arr[index]
        while cur.next!=None:
            cur=cur.next
            if cur.data[0]==key:
                found=True
                return cur.data[1]
        if not found:
            print(f'{key} not in hashmap')
            return
    def __delitem__(self,key):
        found=False
        index=self.hash_func(key)
        cur=self.arr[index]
        while cur.next!=None:
            last_node=cur
            cur=cur.next
            if cur.data[0]==key:
                found=True
                last_node.next=cur.next
        if not found:
            print(f'{key} is not in hashmap')
            return
