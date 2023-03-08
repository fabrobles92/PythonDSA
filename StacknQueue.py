class Stack:
    def __init__(self) -> None:
        self.elements = []
    
    def push(self, value):
        self.elements.append(value)

    def pop(self):
        if self.check_empty():
            return None
        return self.elements.pop(len(self.elements) - 1)

    def check_empty(self):
        return len(self.elements) == 0

    def peek(self):
        return self.elements[len(self.elements) - 1]


class Queue:
    def __init__(self) -> None:
        self.elements = []
    
    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        if self.check_empty():
            return None
        return self.elements.pop(0)

    def check_empty(self):
        return self.elements == 0

    def peek(self):
        if self.check_empty():
            return None
        return self.elements[0]



class CircularQueue():
    def __init__(self, k) -> None:
        self.k = k
        self.items = [None] * self.k
        self.front = - 1
        self.rear = - 1

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            return print('Queue is empty')
        elif self.front == self.rear:
            temp = self.items[self.front]
            self.front = - 1
            self.rear = - 1
            return temp
        else:
            temp = self.items[self.front]
            self.front = (self.front + 1 ) % self.k
            return temp

    def enqueue(self, value):
        if (self.rear  + 1) % self.k == self.front:
            return print('Queue is full')
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.items[self.front] = value
        else:
            self.tail = (self.tail + 1) % self.k
            self.items[self.tail] = value
    

class DoubleEndedQueue():
    def __init__(self, k) -> None:
        self.k = k
        self.elements = [None] * self.k
        self.front = -1
        self.rear = 0
    
    def insert_front(self, value):
        if self.front == -1:
            self.front = 0
            self.elements[self.front] = value
        elif (self.rear + 1) % self.k == self.front:
            print('Queue Overflow')
        else:
            self.front = (self.front - 1) % self.k
            self.elements[self.front] = value 

    def insert_rear(self, value):
        if self.front == -1:
            self.front = 0
            self.elements[self.rear] = value
        elif (self.rear + 1) % self.k == self.front:
            print('Queue overflow')
        else:
            self.rear = (self.rear + 1) % self.k
            self.elements[self.rear] = value

    def remove_front(self):
        if self.front == -1:
            return print('Queue empty')
        elif self.front == self.rear:
            temp = self.elements[self.front]
            self.elements[self.front] = None
            self.front = -1
            self.rear = 0
            
            return temp
        else:
            temp =  self.elements[self.front]
            self.elements[self.front] = None
            self.front = (self.front + 1) % self.k
            return temp
        
    def remove_rear(self):
        if self.front == -1:
            return print('Queue empty')    
        elif self.front == self.rear:
            temp = self.elements[self.rear]
            self.elements[self.rear] = None
            self.front = -1
            self.rear = 0
            return temp
        else:
            temp = self.elements[self.rear]
            self.elements[self.rear] = None
            self.rear = (self.rear - 1) % self.k
            return temp


