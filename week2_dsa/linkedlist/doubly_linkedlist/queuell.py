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
    
class Queue():
    size = 0
    def __init__(self):
        self.front = None
        self.rear = None
    
    def insert_node_last(self):
        student = Student()
        data = student.create_student()
        node = Node(data)

        self.size += 1
        if self.front == None:
            self.front = node
            self.rear = node
            print("Insertion of first node done")
            return
        
        node.prev = self.rear
        self.rear.next = node
        self.rear = node

        print("Insertion of node done at last.")
    
    def delete_node_first(self):
        if self.front == None:
            print("Stack is Empty, Delection Cant done.")
            return
        
        self.size -= 1
        if self.front.next == None:
            self.front = None
            self.rear = None
            return

        self.front = self.front.next
        self.front.prev = None

        print("Delection of node done at first.")

    def insert_at_position(self, position):
        if position < 1 or position > self.size+1:
            print("Invaild position to Insert.")
            return
        
        if position == 1:
            self.insert_node_first()
            return
        
        if self.size == position-1:
            self.insert_node_last()
            return

        student = Student()
        data = student.create_student()
        node = Node(data)
        self.size += 1

        pos = 1
        curr_node = self.front
        while pos < position-1 and curr_node != None:
            curr_node = curr_node.next
            pos += 1
        next_nodes = curr_node.next
        curr_node.next = node
        node.prev = curr_node
        node.next = next_nodes
        next_nodes.prev = node
        print("Insertion of node done at", position)

    def delete_at_position(self, position):
        if position < 1 or position > self.size:
            print("Invaild position to Delete.")
            return
        
        if position == 1:
            self.delete_node_first()
            return
        
        if self.size == position:
            self.delete_node_last()
            return
        
        self.size -= 1
        pos = 1
        curr_node = self.front
        while pos < position-1 and curr_node != None:
            curr_node = curr_node.next
            pos += 1
        next_node = curr_node.next
        next_nodes = next_node.next
        curr_node.next = next_nodes
        next_nodes.prev = curr_node

        print("Delection of node done at", position)
  
    def delete_node_last(self):
        if self.front == None:
            print("Stack is empty, Delection cant done.")
            return
        
        self.size -= 1
        if self.front.next == None:
            self.front = None
            self.rear = None
            return

        self.rear = self.rear.prev
        self.rear.next = None

        print("Delection of node done at last.")

    def insert_node_first(self):
        student = Student()
        data = student.create_student()
        node = Node(data)

        self.size += 1
        if self.front == None:
            self.front = node
            self.rear = node
            print("Insertion of first node is done")
            return
        
        node.next = self.front 
        self.front.prev = node
        self.front = node

        print("Insertion of node done at first.")

    def print_list_forward(self):
        if self.front == None:
            print("Queue is empty")
            return
        
        print("List of students -> ")
        temp = self.front
        while temp != None:
            temp.print_node_data()
            temp = temp.next

    def print_list_backward(self):
        if self.front == None:
            print("Queue is empty")
            return
        
        print("List of students in reverse -> ")
        temp = self.rear
        while temp != None:
            temp.print_node_data()
            temp = temp.prev

queue = Queue()
queue.insert_node_last()
queue.insert_node_last()
queue.insert_node_last()
queue.insert_at_position(1)
queue.insert_at_position(2)
# queue.insert_at_position(6)
# queue.insert_at_position(9)
# queue.delete_node_last()
# queue.insert_node_first()
queue.print_list_forward()
# queue.delete_node_first()
queue.print_list_backward()
queue.delete_at_position(1)
queue.delete_at_position(3)
queue.delete_at_position(9)
# queue.delete_node_last()
# queue.insert_node_first()
# queue.insert_node_last()
# queue.insert_node_first()
# queue.insert_node_last()
# queue.delete_node_last()
queue.print_list_forward()
# queue.delete_node_first()
queue.print_list_backward()