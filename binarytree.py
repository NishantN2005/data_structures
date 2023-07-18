class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:return False

    """InOrder Traversal: O(N)
        1.)go left and perform action
        2.)perform action on current
        3.)go right and perform action"""
    
    def in_order_traversal(self):
        elements=[]
        #visit left tree
        if self.left:
            elements+=self.left.in_order_traversal()
        #visit root node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    """PreOrder Traversal:
        1.)perform action on current
        2.)go left and perform action
        3.)go right and perform action"""
    
    def pre_order_traversal(self):
        elements=[self.data]
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements
    
    """PostOrder Traversal:
    1.)go left and perform action
    2.)go right and perform action
    3.)perform action on current"""

    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    def find_max(self):
        if self.right==None:
            return self.data
        return self.right.find_max()
    def find_min(self):
        if self.left==None:
            return self.data
        return self.left.find_min()
    def sum(self):
        sum=0
        if self.left:
            sum+=self.left.sum()
        sum+=self.data
        if self.right:
            sum+=self.right.sum()
        return sum
    """3 cases:
        1: Delete node wiht no child-just delete
        2: Delete node with 1 child-move child up
        3: Dete node with 2 children-find the min on the right and move it up OR find max on the left and move it up"""
    def delete(self,val):
        #searching for val
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)    
        #once we find val and only 1 child
        else:
            if self.left==None and self.right==None:
                return None
            elif self.left==None:
                return self.right
            elif self.right==None:
                return self.left
        #once we find val and there are 2 children
        max_val=self.left.find_max()
        self.data=max_val
        #get rid of duplicate by finding min_val again
        self.left=self.left.delete(max_val)
        return self
def build_tree(elements):
    root=BinarySearchTree(elements[0]) 
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
numbers=[17,4,1,20,9,23,18,34]
numbers_tree=build_tree(numbers)
numbers_tree.delete(20)
print(numbers_tree.in_order_traversal())