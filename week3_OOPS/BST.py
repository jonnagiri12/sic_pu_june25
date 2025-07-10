class Node():
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
    
class BST():
    def __init__(self):
        self.root = None
    
    def add_node(self, data):
        new_node = Node(data)

        if self.root == None:
            self.root = new_node
            print("Root node is created")
            return
        
        temp1 = self.root
        temp2 = None

        while temp1 != None:
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node
    
    def in_order(self, root):
        if root != None:
            self.in_order(root.left)
            print(root.data, end = " ")
            self.in_order(root.right)

    def pre_order(self, root):
        if root != None:
            print(root.data, end = " ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root != None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end = " ")

bst = BST()
bst.add_node(10)
bst.add_node(20)
bst.add_node(30)
bst.add_node(40)
bst.add_node(50)
bst.pre_order(bst.root)
print()
bst.in_order(bst.root)
print()
bst.post_order(bst.root)