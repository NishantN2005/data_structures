class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        i=0
        p=self.parent
        while p:
            i+=1
            p=p.parent
        return i
    def print_tree(self):
        spaces=" "*self.get_level()*5
        prefix=spaces+"|__" if self.parent else""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root=Treenode("electronics")

    laptop=Treenode("laptop")
    laptop.add_child(Treenode('macbook'))
    laptop.add_child(Treenode("Surface"))
    laptop.add_child(Treenode("Windows"))

    cellphone=Treenode("cellphone")
    cellphone.add_child(Treenode("iPhone"))
    cellphone.add_child(Treenode("Google"))
    cellphone.add_child(Treenode("Vivo"))

    tv=Treenode("tv")
    tv.add_child(Treenode("samsung"))
    tv.add_child(Treenode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root
root=build_product_tree()
root.print_tree()