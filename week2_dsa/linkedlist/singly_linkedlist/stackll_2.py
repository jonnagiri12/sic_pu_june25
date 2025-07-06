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

    def insert_node_last(self):
        student = Student()
        data = student.create_student()
        node = Node(data)

        if self.front == None:
            self.front = node
            return
        
        temp = self.front
        while temp.link != None:
            temp = temp.link
        temp.link = node
        print("Insertion of node at last is done")
   
    def delete_node_last(self):
        if self.front == None:
            print("Stack is empty, delection of node cant be done.")
            return

        if self.front.link == None:
            self.front = None
            return

        last_second_node = self.front
        last_node = self.front.link
        while last_node.link != None:
            last_second_node = last_node
            last_node = last_node.link
        
        last_second_node.link = None
        print("Delection of node at last is done")
    
    def print_list(self):
        if self.front == None:
            print("Stack is empty")
            return
        
        temp = self.front
        while temp != None:
            temp.print()
            temp = temp.link

stack = Stack()
stack.insert_node_last()
stack.insert_node_last()
stack.insert_node_last()
stack.print_list()