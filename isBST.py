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


def isbst(root):
    def helper(root,min,max):
        if root is None:
            return True
        if root.getData() <= min and root.getData() >= max:
            return False
        leftbst = helper(root.getLeft(), min, root.getData())
        rightbst = helper(root.getRight(), root.getData(), max)
        return leftbst and rightbst
        
    return helper (root,float("-infinity"), float("infinity"))

    
def main():
    root            = BinaryTreeNode(5)
    root.left       = BinaryTreeNode(199)
    root.right      = BinaryTreeNode(21)
    root.left.left  = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(45)
    root.right.left = BinaryTreeNode(1)
    root.right.right = BinaryTreeNode(-1)
    print (isbst(root))
     
if __name__ == '__main__':
    main()
