class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def get_element(self, position):
        temp = self.head
        for i in range(position):
            if temp == None:
                return None
            temp = temp.next
        return temp.value

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        temp = self.head
        new_node = Node(value)
        new_node.next = None
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
    
    def insert_after_node(self, prev_node, value):        
        if not prev_node:
            print('Node must be in the list')
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, pos):
        if not self.head:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            return
        i = 1
        while i < pos:            
            temp = temp.next
            i+=1
            if temp.next == None:
                return print('Position does not exist in List')
        
        temp.next = temp.next.next

    def search(self, value):
        temp = self.head
        pos = 0
        while temp != None:
            if temp.value == value:
                return pos
            pos += 1
            temp = temp.next

    def reverse_linked_list(self):
        previous = None
        temp = self.head
        while temp != None:
            next_node = temp.next
            temp.next = previous
            previous = temp
            temp = next_node
        return previous

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_start(self, val):
        new_node = Node(val)
        temp = self.head
        if temp is not None:
            temp.previous = new_node
        self.head = new_node
        self.head.next = temp

    def insert_end(self, val):
        new_node = Node(val)        
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        new_node.previous = temp
        temp.next = new_node

    def insert_after(self, prev_node, val):
        new_node = Node(val)
        if prev_node == None:
            return print('No previous node was given')
        new_node.next = prev_node.next
        new_node.previous = prev_node
        prev_node.next = new_node
        if new_node.next:
            new_node.next.previous = new_node

    def delete(self, dele):
        if dele is None or self.head is None:
            return print('Impossible to delete')
        temp = self.head

        if dele == self.head:
            self.head = temp.next
            if self.head:
                self.head.previous = None
            return
        
        dele.previous.next = dele.next
        if dele.next is not None:
            dele.next.previous = dele.previous
        
    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

class CircularDoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_start(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.head.previous = self.head
            self.head.next = self.head
            return
        temp  = self.head

        if self.head == self.head.previous:
            self.head = new_node
            self.head.next = temp
            self.head.previous = temp
            temp.previous = self.head
            temp.next = self.head    
            return

        self.head = new_node
        self.head.previous = temp.previous
        self.head.previous.next = self.head
        self.head.next = temp
        temp.previous = self.head
        
        

    def insert_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.head.previous = self.head
            self.head.next = self.head
            return

        temp = self.head
        if self.head.next == self.head:            
            self.head.next = new_node
            self.head.previous = new_node
            new_node.next = self.head
            new_node.previous = self.head
            return
        
        new_node.previous = self.head.previous
        new_node.next = self.head
        new_node.previous.next = new_node
        self.head.previous = new_node

    def insert_after(self, prev_node, val):
        if prev_node is None:
            return print('Impossible to add')
        new_node = Node(val)

        new_node.next = prev_node.next
        new_node.previous = prev_node
        prev_node.next.previous = new_node
        prev_node.next = new_node

    def delete(self, node):
        if node is None:
            return print('Impossible to delete')
        
        if self.head == self.head.next:
            self.head = None
            return

        if node == self.head:
            if node.previous == node.next:
                self.head = node.next
                self.head.previous = self.head.next = self.head
            else:
                self.head = node.next
                self.head.previous = node.previous
                node.previous.next = self.head
            node = None
            return

        node.previous.next = node.next
        node.next.previous = node.previous
        node = None
        
    def traverse_list(self, reverse=False):
        if self.head:
            if reverse:
                print(self.head.previous.value)
                temp = self.head.previous.previous
                while temp != self.head.previous:
                    print(temp.value)
                    temp = temp.previous
            else:
                print(self.head.value)
                temp = self.head.next
                while temp != self.head:
                    print(temp.value)
                    temp = temp.next
        return
