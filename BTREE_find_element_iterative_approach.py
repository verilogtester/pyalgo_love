"""Same as level traversal, instead of capturing result, compare the data and return 1 if found, else 0"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data    # Root Node
        self.left = None    # Left Child
        self.right = None   # Right Child
        
    # set data
    def setData(self, data):
        self.data = data
    
    # get data
    def getData(self):
        return self.data
    
    # get left child of a node
    def getLeft(self):
        return self.left
    
    # get right child of a node
    def getRight(self):
        return self.right

import queue
def iter_find_data_in_tree(root,data): 
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    node = None
    result = []
    while not q.empty():
        node = q.get() # Dequeue FIFO
        if node.getData() == data:
            return 1
        if node.getLeft() is not None:
            q.put(node.getLeft())
        if node.getRight() is not None: 
            q.put(node.getRight())
            
    return 0
    
def main():
    root            = BinaryTreeNode(5)
    root.left       = BinaryTreeNode(199)
    root.right      = BinaryTreeNode(21)
    root.left.left  = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(45)
    root.right.left = BinaryTreeNode(1)
    root.right.right = BinaryTreeNode(-1)
    print ("element found in the Binary Tree is : ", iter_find_data_in_tree(root, 45))
    print ("element found in the Binary Tree is : ", iter_find_data_in_tree(root, 145))   
     
if __name__ == '__main__':
    main()
