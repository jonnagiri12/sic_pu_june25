class Node():
    def __init__(self, data):
        self.data = data
        self.link = None
    
class Circular_linkedlist():
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    delected_elements = []
    
    def insert_first(self, data):
        node = Node(data)
        
        self.size += 1
        if self.front == None:
            self.front = self.rear = node
            self.rear.link = self.front
            print("Insertion of first node done.")
            return
        
        node.link = self.front
        self.front = node
        self.rear.link = self.front
        print("Insertion of node at first.")

    def insert_last(self, data):
        node = Node(data)
        
        self.size += 1
        if self.front == None:
            self.front = self.rear = node
            print("Inserction of first node done.")
            return 
        
        self.rear.link = node
        node.link = self.front
        self.rear = node
        print("Insertion of node done at last.")

    def delete_first(self):
        if self.front == None:
            print("Delection of node is not possible, List is Empty")
            return
        
        self.size -= 1
        if self.front == self.rear :
            self.front = self.rear = None
            print("Delection of node done at first, list is Empty.")
            return
        
        self.delected_elements.append(self.front.data)
        self.front = self.front.link
        self.rear.link = self.front
        print("Delection of node done at first")
        print("Delected elemnts :", self.delected_elements)
        
    def delete_last(self):
        if self.front == None:
            print("Delction of node not possible, List is Empty")
            return
        
        self.size -= 1
        if self.front == self.rear :
            self.front = self.rear = None
            print("Delection of node done at first, list is Empty.")
            return
        
        temp = self.front
        while temp.link != self.rear:
            temp = temp.link
        temp.link = self.front
        self.rear = temp
        self.delected_elements.append(self.rear.data)
        print("Delection of last node done at last.")
        print("Delected elemnts :", self.delected_elements)

    def insert_at_position(self, position, data):
        if position < 1 or position > self.size+1:
            print("Invaild position to Insert.")
            return
        
        if position == 1:
            self.insert_first(data)
            return
        
        if self.size == position-1:
            self.insert_last(data)
            return

        node = Node(data)
        self.size += 1

        pos = 1
        curr_node = self.front
        while pos < position-1:
            curr_node = curr_node.link
            pos += 1
        next_nodes = curr_node.link
        curr_node.link = node
        node.link = next_nodes
        print("Insertion of node done at", position)

    def delete_at_position(self, position):
        if position < 1 or position > self.size:
            print("Invaild position to Delete.")
            return
        
        if position == 1:
            self.delete_first()
            return
        
        if self.size == position:
            self.delete_last()
            return
        
        self.size -= 1
        pos = 1
        curr_node = self.front
        while pos < position-1:
            curr_node = curr_node.link
            pos += 1
        next_node = curr_node.link
        self.delected_elements.append(next_node.data)
        next_nodes = next_node.link
        curr_node.link = next_nodes
        print("Delection of node done at", position)

    def print_list(self):
        if self.front == None:
            print("List is Empty")
            return 
        
        loop = True
        temp = self.front
        while loop:
            print(temp.data, end =  "->")
            temp = temp.link
            if (temp == self.front):
                loop = False
        print("HEAD")   

circularll = Circular_linkedlist()
circularll.insert_last(10)
circularll.insert_last(20)
circularll.insert_last(30)
circularll.insert_first(40)
circularll.insert_first(50)
circularll.print_list()
circularll.insert_at_position(1, 60)
circularll.insert_at_position(7, 70)
circularll.insert_at_position(9, 70)
circularll.print_list()
circularll.delete_first()
circularll.delete_first()
circularll.delete_last()
# circularll.insert_first(60)
# circularll.insert_first(70)
circularll.print_list()