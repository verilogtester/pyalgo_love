"""Assumption - find maximum depth of a tree
    def max_depth(node):
base -> if node is None:
            return float('inf') # Largest floating point infinite number
generic-> 
        max_depth = max (max_depth(node.left), max_depth(node.right) + 1
"""

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

def find_recursive(root, data):
    if root is None:
        return 0
    
    if root.getData() == data:
        return 1
    else:
        temp = find_recursive(root.left, data)
        if temp == 1:
            return temp
        else:
            return find_recursive(root.right, data)
    
def main():
    root            = BinaryTreeNode(5)
    root.left       = BinaryTreeNode(199)
    root.right      = BinaryTreeNode(21)
    root.left.left  = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(45)
    root.right.left = BinaryTreeNode(1)
    root.right.right = BinaryTreeNode(-1)
    print ("Maximum element in the Binary Tree is : ", find_recursive(root, 45))
    print ("Maximum element in the Binary Tree is : ", find_recursive(root, 145))   
     
if __name__ == '__main__':
    main()
