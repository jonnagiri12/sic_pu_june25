# Implement Stack using list, insert and delete from rear of the list

import sys

arr = []
def push(num):
    arr.append(num)

def pop():
    if len(arr) == 0:
        print("Stack is empty!")
        return
    arr.pop()

def prt():
    if len(arr) == 0:
        print("Stack is empty!")
        return
    print(arr)

def invaild():
    print("invaild choice! ")
    sys.exit()

def stack(choice):
    if choice == 1:
        num = int(input("Enter value to push : "))
    
    match(choice):
        case 1: push(num)
        case 2: pop()
        case 3: prt()
        case 4: sys.exit()
        case _: invaild()

while True:
    print("1. Push\n2. Pop\n3. Print\n4. Exit")
    choice = int(input("Enter choice : "))
    stack(choice)


# Implement Stack using list, insert and delete from front of the list

# import sys

# arr = []
# def push(num):
#     arr.insert(0, num)

# def pop():
#     if len(arr) == 0:
#         print("Stack is empty!")
#         return
#     del arr[0]

# def prt():
#     if len(arr) == 0:
#         print("Stack is empty!")
#         return
#     print(arr)

# def invaild():
#     print("invaild choice! ")
#     sys.exit()

# def stack(choice):
#     if choice == 1:
#         num = int(input("Enter value to push : "))
    
#     match(choice):
#         case 1: push(num)
#         case 2: pop()
#         case 3: prt()
#         case 4: sys.exit()
#         case _: invaild()

# while True:
#     print("1. Push\n2. Pop\n3. Print\n4. Exit")
#     choice = int(input("Enter choice : "))
#     stack(choice)


# Implement Queue using list, insert at rear delete from front the list

# import sys 

# arr = []
# def enqueue(num):
#     arr.append(num)

# def dequeue():
#     if len(arr) == 0:
#         print("Queue is empty!")
#         return
#     del arr[0]

# def print_queue():
#     if len(arr) == 0:
#         print("Queue is empty!")
#         return
#     print(arr)

# def invaild():
#     print("invaild choice! ")
#     sys.exit()

# def queue(choice):
#     if choice == 1:
#         num = int(input("Enter value to push : "))
    
#     match(choice):
#         case 1: enqueue(num)
#         case 2: dequeue()
#         case 3: print_queue()
#         case 4: sys.exit()
#         case _: invaild()

# while True:
#     print("1. Enqueue\n2. Dequeue\n3. Print Queue\n4. Exit")
#     choice = int(input("Enter choice : "))
#     queue(choice)

# Implement Queue using list, insert front, delete from rear of the list

# import sys 

# arr = []
# def enqueue(num):
#     arr.insert(0, num)

# def dequeue():
    # if len(arr) == 0:
    #     print("Queue is empty!")
    #     return
#     arr.pop()

# def print_queue():
#     if len(arr) == 0:
#         print("Queue is empty!")
#         return
#     print(arr)

# def invaild():
#     print("invaild choice! ")
#     sys.exit()

# def queue(choice):
#     if choice == 1:
#         num = int(input("Enter value to push : "))
    
#     match(choice):
#         case 1: enqueue(num)
#         case 2: dequeue()
#         case 3: print_queue()
#         case 4: sys.exit()
#         case _: invaild()

# while True:
#     print("1. Enqueue\n2. Dequeue\n3. Print Queue\n4. Exit")
#     choice = int(input("Enter choice : "))
#     queue(choice)