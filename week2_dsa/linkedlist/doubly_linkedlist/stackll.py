class Node():
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

    def print_node_data(self):
        print(f"ID = {self.data[0]} Name = {self.data[1]} Marks = {self.data[2]}")

class Student():
    def create_student(self):
        id = int(input("Enter id of student : "))
        name = input("Enter name of student : ")
        marks = float(input("Enter marks of student : "))
        student_details = [id, name, marks]
        return student_details
    
class Stack():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def insert_node_last(self):
        student = Student()
        data = student.create_student()
        node = Node(data)

        if self.front == None:
            self.front = node
            self.rear = node
            print("Insertion of first node done")
            return
        
        node.prev = self.rear
        self.rear.next = node
        self.rear = node

        print("Insertion of node done at last.")

    def delete_node_last(self):
        if self.front == None:
            print("Stack is empty, Delection cant done.")
            return

        if self.front.next == None:
            self.front = None
            self.rear = None
            return

        self.rear = self.rear.prev
        self.rear.next = None

        print("Delection of node done at last.")
    
    def delete_node_first(self):
        if self.front == None:
            print("Stack is Empty, Delection Cant done.")
            return

        if self.front.next == None:
            self.front = None
            self.rear = None
            return

        self.front = self.front.next
        self.front.prev = None

        print("Delection of node done at first.")
  
    def insert_node_first(self):
        student = Student()
        data = student.create_student()
        node = Node(data)

        if self.front == None:
            self.front = node
            self.rear = node
            print("Insertion of first node done")
            return
        
        node.next = self.front 
        self.front.prev = node
        self.front = node

        print("Insertion of node done at first.")
    
    def print_list_forward(self):
        if self.front == None:
            print("Stack is empty")
            return
        
        print("List of students -> ")

        temp = self.front
        while temp != None:
            temp.print_node_data()
            temp = temp.next

    def print_list_backward(self):
        if self.front == None:
            print("Stack is empty")
            return
        
        print("List of students in reverse -> ")
        temp = self.rear
        while temp != None:
            temp.print_node_data()
            temp = temp.prev

stack = Stack()
stack.insert_node_last()
stack.insert_node_last()
stack.insert_node_last()
stack.delete_node_last()
stack.insert_node_first()
stack.insert_node_first()
stack.print_list_forward()
stack.delete_node_first()
stack.print_list_backward()
stack.delete_node_last()
stack.insert_node_first()
stack.insert_node_last()
stack.delete_node_last()
stack.delete_node_first()
stack.print_list_backward()