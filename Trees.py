import heapq

class MaxHeap:
    def __init__(self, arr = []) -> None:
        self.arr = arr        

    def heapify(self):
        size = len(self.arr)
        for i in range((size // 2) - 1, -1, -1):
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < size and self.arr[i] < self.arr[left]:
                largest = left
            if right < size and self.arr[largest] < self.arr[right]:
                largest = right
            if largest != i:
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]

    def insert(self, value):  
        self.arr.append(value)
        size = len(self.arr)

        # for i in range((size//2) - 1, -1, -1):
        #     self.heapify(size, i)
        self.heapify()

    def delete(self, value):
        size = len(self.arr)
        if size == 1:
            self.arr = []
        else:
            index = 0
            while index < size:
                if self.arr[index] == value:
                    break
                index += 1

            if index < size:
                self.arr[index], self.arr[size - 1] = self.arr[size - 1], self.arr[index]
                self.arr.pop()
            
            # for i in range((len(self.arr) // 2) - 1, -1, -1):
            #     self.heapify(len(self.arr), i)
            self.heapify()


    def pop(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        popped_value =  self.arr.pop()
        # size = len(self.arr)
        # for i in range((size // 2) - 1, -1, -1):
        #     self.heapify(size, i)
        self.heapify()
        return popped_value
    def find_max(self):
        return self.arr[0]

class MinHeap:
    def __init__(self, arr = []) -> None:
        self.arr = arr

    def heapify(self):
        size = len(self.arr)
        for i in range((size//2 - 1), -1, -1):
            shortest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < size and self.arr[i] > self.arr[left]:
                shortest = left
            if right < size and self.arr[shortest] > self.arr[right]:
                shortest = right

            if shortest != i:
                self.arr[i], self.arr[shortest] = self.arr[shortest], self.arr[i]


    def insert(self, value):
        self.arr.append(value)
        size = len(self.arr)

        # for i in range((size // 2) - 1, -1, -1):
        #     self.heapify(size, i)
        self.heapify()

    def delete(self, value):
        i = 0
        while i < len(self.arr):
            if self.arr[i] == value:
                break
            i += 1
        if i < len(self.arr):
            self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
            self.arr.pop()
            # size = len(self.arr)
            # for i in range( (size // 2) - 1, -1, -1):
            #     self.heapify(size, i)
            self.heapify()
        else:
            print('Value not found')

    def pop(self):
        if len(self.arr) < 1:
            return print('Not possible to delete empty queue')
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        popped_number = self.arr.pop()
        # size = len(self.arr)
        # for i in range((size // 2) - 1 , -1, -1):
        #     self.heapify(size, i)
        self.heapify()
        return popped_number

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root) -> None:
        self.root = root
        self.depth =  self.calculate_depth(self.root)
        self.number_nodes = self.count_nodes(self.root)

    def calculate_depth(self, root):
        d = 0
        while root is not None:
            d += 1
            root = root.left
        return d
    
    def count_nodes(self, root):

        if not root:
            return 0
        
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)



    #Left => Node =>  Right
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

    #Node => Left => Right
    def preorder(self, root):
        if root:
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right)

    #Left => Right => Root
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value)


    def isFullBinaryTree(self, root):
        if not root:
            return True
        
        if root.left is None and root.right is None:
            return True
        
        if root.left is not None and root.right is not None:
            return self.isFullBinaryTree(root.left) and self.isFullBinaryTree(root.right)

        return False

    def isPerfectBinaryTree(self, root, level=0):

        if not root:
            return True

        if root.left is None and root.right is None:
            return self.depth == level + 1

        if root.left is not None and root.right is not None:
            return self.isPerfectBinaryTree(root.left, level + 1) and self.isPerfectBinaryTree(root.right, level + 1)
        
        return False
    
    def isCompleteBinaryTree(self, root, index = 0):

        if not root:
            return True
        
        if index >= self.number_nodes:
            return False
        
        return self.isCompleteBinaryTree(root.left, 2 * index + 1) and self.isCompleteBinaryTree(root.right, 2 * index + 2)
    
    def isBalancedBinaryTree(self, root):

        if not root:
            return 0

        left_height = self.isBalancedBinaryTree(root.left)

        if left_height == -1:
            return -1
        
        right_height = self.isBalancedBinaryTree(root.right)

        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1 
    
class BinarySeachTree:
    def __init__(self, root) -> None:
        self.root = root

    def insert(self, root, value):

        if root is None:
            return Node(value)
            
        if value < root.value:
            root.left = self.insert(root.left, value)

        if value > root.value:
            root.right = self.insert(root.right, value)
        return root

    def search(self, root, value):
        if root is None:
            return None
        
        if root.value == value:
            return root
        
        if value < root.value:
            return self.search(root.left, value)
        
        if value > root.value:
            return self.search(root.right, value)
        

    def getmin_node(self, root):
        if root.left is not None:
            return self.getmin_node(root.left)
        return root

    def delete(self, root, value):
        if root is None:
            return None
        
        if root.value == value:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp = self.getmin_node(root.right)
                root.value = temp.value
                root.right = self.delete(root.right, temp.value)

        if value < root.value:
            root.left = self.delete(root.left, value)
        if value > root.value:
            root.right = self.delete(root.right, value)

        return root

"""Module methods"""
#Heap Sort 
def heapify(arr, size, i, min):
        shortest = i
        left = 2*i + 1
        right = 2*i + 2
        if min:
            if left < size and arr[i] > arr[left]:
                shortest = left

            if right < size and arr[shortest] > arr[right]:
                shortest = right
        else:
            if left < size and arr[i] < arr[left]:
                shortest = left

            if right < size and arr[shortest] < arr[right]:
                shortest = right

        if shortest != i:
            arr[i], arr[shortest] = arr[shortest], arr[i]
            heapify(arr, size, shortest, min)

def heap_sort(arr, min=True):
    size = len(arr)

    for i in range((size //2 ) - 1, -1, -1):
        heapify(arr, size, i, min)

    return arr
 
#Traverse Binary tree
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def preoder(root):
    if root is None:
        return
    print(root.value)
    preoder(root.left)
    preoder(root.right)
    
def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.value)

#Check Tree Kind
def isFullBinaryTree(root):
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return True
    
    if root.left is not None and root.right is not None:
        return isFullBinaryTree(root.left) and isFullBinaryTree(root.right)
    
    return False

def calculate_deepth(root):
    deep = 0
    while root is not None:
        deep += 1
        root = root.left
    return deep

def isPerfectBinaryTree(root, deep, level=0):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return deep == level + 1
    
    if root.left is not None and root.right is not None:
        return False
    
    return isPerfectBinaryTree(root.left, deep, level + 1) and isPerfectBinaryTree(root.right, deep, level + 1)

def calculate_num_nodes(root):
    if root is None:
        return 0
    
    return (calculate_num_nodes(root.left) + calculate_num_nodes(root.right)) + 1

def isCompleteBinaryTree(root, num_nodes, index=0):
    if root is None:
        return True
    if index >= num_nodes:
        return False
    
    return isCompleteBinaryTree(root.left, num_nodes, 2 * index + 1) and isCompleteBinaryTree(root.right, num_nodes, 2 * index + 2)

def isBalancedBinaryTree(root):
    if root is None:
        return 0

    left_height = isBalancedBinaryTree(root.left)

    if left_height == -1:
        return -1
    
    right_height = isBalancedBinaryTree(root.right)

    if right_height == -1:
        return -1
    

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1

#BST Operations
def  insert(root, value):
    if root is None:
        return Node(value)
    
    if  value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root
    
def search(root, value):
    if root is None:
        return None
    if value == root.value:
        return root
    elif value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)

def get_min_node(root):
    if root.left is None:
        return root
    return get_min_node(root.left)
    
def delete(root, value):
    if root is None:
        return None
    
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        root.value = get_min_node(root.right).value
        root.right = delete(root.right, root.value)
        
    return root
   