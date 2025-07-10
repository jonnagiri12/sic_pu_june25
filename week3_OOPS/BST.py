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

    def search_node(self, root, target):
        if root != None:
            if root.data == target:
                return True
            elif root.data < target:
                return self.search_node(root.right, target)
            elif root.data > target:
                return self.search_node(root.left, target)
        return False
    
    def delete_node(self, data):
        temp1 = self.root
        temp2 = None
        while temp1.data != data:
            temp2 = temp1
            if data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        # temp1 now points to node to be deleted and temp2 points to its parent.
        print(f'Node with data {temp1.data} deleted')

        if temp1 is self.root:
            if temp1.left is None and temp1.right is None:
                self.root = None
            if temp1.left is not None and temp1.right is not None:
                temp3 = temp1.right.left
                if temp3 is None:
                    temp1.right.left = temp1.left
                    self.root = temp1.right
                else:
                    while temp3.left is not None:
                        temp3 = temp3.left
                    temp3.left = temp1.left
        else:
            # If node to be deleted is a leaf node:
            if temp1.left is None and temp1.right is None:            
                if temp2 is None:
                    self.root = None
                elif temp2.left is temp1:
                    temp2.left = None
                else:
                    temp2.right = None

            # If node to be deleted has 2 children
            elif temp1.left is not None and temp1.right is not None:
                temp3 = temp1.right.left
                if temp3 is None:
                    temp1.right.left = temp1.left
                else:
                    while temp3.left is not None:
                        temp3 = temp3.left
                    temp3.left = temp1.left
                # if root is the node being deleted
                if temp1 is self.root:
                    self.root = temp1.right
                elif temp2.left is temp1:
                    temp2.left = temp1.right
                else:
                    temp2.right = temp1.right

            # when node to be deleted has exactly one child
            else:
                #link = return () if temp1.left temp1.left else temp1.right
                link = temp1.left # assume temp1 has left child
                if temp1.right:
                    link = temp1.right
                if temp2.left is temp1:
                    temp2.left = link
                else:
                    temp2.right = link

class Menu():
    def __init__(self):
        self.chioce = 0
    
    def tree_empty(self, bst):
        if bst.root == None:
            print("Tree is Empty")
            return False
        
    def menu(self, bst):
        match self.chioce:
            case 1: 
                data = int(input("Enter data : "))
                bst.add_node(data)
            case 2:
                if self.tree_empty(bst):
                    return
                bst.pre_order(bst.root)
            case 3:
                if self.tree_empty(bst):
                    return
                bst.in_order(bst.root)
            case 4:
                if self.tree_empty(bst):
                    return
                bst.post_order(bst.root)
            case 5:
                if self.tree_empty(bst):
                    return
                target = int(input("Enter target : "))
                found = bst.search_node(bst.root, target)
                if found:
                    print(f"Key found")
                else:
                    print(f"Key not found")
            case 6:
                data = int(input("Enter data to be deleted : "))
                bst.delete_node(data)
            case 7:
                self.chioce = 7
            case _:
                print("Invaild chioce.")

    def start_app(self):
        bst = BST()
        while True:
            print("1. Add node\n2. preorder\n3. Inorder\n4. postorder\n5. Search node\n6. Delete node\n7 . Exit")
            self.chioce = int(input("Enter chioce : "))
            self.menu(bst)
            if self.chioce == 7:
                break

menu = Menu()
menu.start_app()     