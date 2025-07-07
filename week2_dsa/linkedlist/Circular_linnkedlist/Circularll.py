class Node():
    def __init__(self, data):
        self.data = data
        self.link = None
    
class Circular_linkedlist():
    def __init__(self):
        self.front = None
        self.rear = None
    
    delected_elements = []
    
    def insert_first(self, data):
        node = Node(data)
        
        if self.front == None:
            self.front = self.rear = node
            print("Insertion of first node done.")
            return
        
        node.link = self.front
        self.front = node
        self.rear.link = self.front
        print("Insertion of node at first.")

    def insert_last(self, data):
        node = Node(data)
        
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
        
        elif self.front == self.rear :
            self.front = self.rear = None
            print("Delection of node done at first, list is Empty.")
            return
        
        self.front = self.front.link
        self.rear.link = self.front
        print("Delection of node done at first")
        
    def delete_last(self):
        if self.front == None:
            print("Delction of node not possible, List is Empty")
            return
        
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
circularll.delete_first()
circularll.delete_first()
circularll.delete_first()
circularll.insert_first(60)
circularll.insert_first(70)
circularll.print_list()