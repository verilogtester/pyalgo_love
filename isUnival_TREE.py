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


def unival(root):
    def helper(root,val):
        if root is None:
            return True
        if root.getData() != val:
            return False
        result = helper(root.getLeft(), val)
        result = result and helper(root.getRight(), val)
        return result
        
    return helper (root,5)

    
def main():
    root            = BinaryTreeNode(5)
    root.left       = BinaryTreeNode(5)
    root.right      = BinaryTreeNode(5)
    root.left.left  = BinaryTreeNode(5)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(5)
    root.right.right = BinaryTreeNode(5)
    print (unival(root))
     
if __name__ == '__main__':
    main()
