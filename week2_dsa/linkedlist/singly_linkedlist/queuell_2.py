class Node():
    def __init__(self, student = None):
        self.data = student
        self.link = None

class Student():
    def __init__(self):
        pass
    def create_student(self):
        id = int(input("Enter id of student : "))
        name = input("Enter name of student : ")
        marks = int(input("Enter marks of student : "))
        student_details = [id, name, marks]
        return student_details

class Queue():
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
    
    def delete_node_first(self):
        if self.front == None:
            print("Queue is Empty")
            return

        if self.front.link == None:
            self.front = None
            return
        
        self.front = self.front.link

    def print(self):
        if self.front == None:
            print("Queue is Empty")
            return

        temp = self.front
        while temp!=None:
            print(temp.data)
            temp = temp.link
        
queue = Queue()
queue.insert_node_last()
queue.insert_node_last()
queue.print()