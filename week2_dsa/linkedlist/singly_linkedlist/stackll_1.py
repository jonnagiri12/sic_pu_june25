class Node():
    def __init__(self, data = None):
        self.data = data
        self.link = None

    def print(self):
        print(f"ID = {self.data[0]} Name = {self.data[1]} Marks = {self.data[2]}")

class Student():
    def __init__(self):
        pass
    
    def create_student(self):
        id = int(input("Enter id of student : "))
        name = input("Enter name of student : ")
        marks = int(input("Enter marks of student : "))
        student_details = [id, name, marks]
        return student_details
    
class Stack():
    def __init__(self):
        self.front = None

    def insert_node_first(self):
        student = Student()
        data = student.create_student()
        node = Node(data)

        if self.front == None:
            self.front = node
            return
        
        node.link = self.front
        self.front = node
        print("Insetion of node at first")
    
    def delete_node_first(self):
        if self.front == None:
            print("Stack is Empty, Delection cant be done.")
            return

        if self.front.link == None:
            self.front = None
            return
        
        self.front = self.front.link
        print("Delection of node at first")
    
    def print_list(self):
        if self.front == None:
            print("Stack is empty")
            return
        
        temp = self.front
        while temp != None:
            temp.print()
            temp = temp.link

stack = Stack()
stack.insert_node_first()
stack.insert_node_first()
stack.insert_node_first()
stack.print_list()