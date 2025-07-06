class Node():
    def __init__(self, data = None):
        self.data = data
        self.link = None

class Student():
    def create_student(self):
        id = int(input("Enter ID of student : "))
        name = input("Enter name of student :")
        marks = float(input("Enter marks of student : "))
        student = (id, name, marks)
        return student

class Queue(): #Insert first remove last
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

    def delete_node_last(self):
        if self.front == None:
            print("Queue is empty")
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

    def print(self):
        if self.front == None:
            print("Queue is empty")
            return
        
        temp = self.front
        while temp != None:
            print(temp.data)
            temp = temp.link
        
queue = Queue()
queue.insert_node_first()
queue.insert_node_first()
queue.insert_node_first()
# queue.delete_node_last()
queue.print()