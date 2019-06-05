"""Assumption - find mininum value in the tree
    def min(node):
base -> if node is None:
            return float('inf') # Largest floating point infinite number
generic-> 
        leftmin = min (node.left)
        rightmin = min (node.right)
        return min(node.val, leftmin, rightmin)       

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

def find_min_recursive(root):
    global minData
    
    if root is None:
        return minData
    
    if root.getData() < minData:
        minData = root.getData()
    
    find_min_recursive(root.getLeft())
    find_min_recursive(root.getRight())
    return minData

def main():
    root            = BinaryTreeNode(5)
    root.left       = BinaryTreeNode(19)
    root.right      = BinaryTreeNode(21)
    root.left.left  = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(45)
    root.right.left = BinaryTreeNode(1)
    root.right.right = BinaryTreeNode(-1)

    print ("Minimum element in the Binary Tree is : ",find_min_recursive(root))   
    
if __name__ == '__main__':
    minData = float("infinity")
    main()
