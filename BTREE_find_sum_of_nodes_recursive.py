"""Assumption - find maximum value in the tree
    def max(node):
base -> if node is None:
            return float('inf') # Largest floating point infinite number
generic-> 
        leftmin = max (node.left)
        rightmin = max (node.right)
        return max (node.val, leftmin, rightmin)       

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

def sum_tree_recursive(root):
    if root is None:
        return 0
    
    return sum_tree_recursive(root.left) + \
            sum_tree_recursive(root.right) + \
            root.data

    
def main():
    root            = BinaryTreeNode(5)
    root.left       = BinaryTreeNode(199)
    root.right      = BinaryTreeNode(21)
    root.left.left  = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(45)
    root.right.left = BinaryTreeNode(1)
    root.right.right = BinaryTreeNode(-1)

    print ("Maximum element in the Binary Tree is : ",sum_tree_recursive(root))   
    
if __name__ == '__main__':
    main()
