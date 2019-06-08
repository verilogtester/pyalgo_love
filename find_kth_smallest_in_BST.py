
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

count = 0
def find_kth_elements(root,k):
    global count
    if(not root):
        return None
    
    left = find_kth_elements(root.left,k)
    if (left):
        return left       
    count += 1
    if (count == k):
        return root.data
    
    return find_kth_elements(root.right,k)

def isbst(root):
    def helper(root,min,max):
        if root is None:
            return True
        if root.data <= min and root.data >= max:
            return False
        leftbst = helper(root.left, min, root.data)
        rightbst = helper(root.right, root.data, max)
        return leftbst and rightbst
        
    return helper (root,float("-infinity"), float("infinity"))

            
def main():
    root            = BinaryTreeNode(4)
    root.left       = BinaryTreeNode(2)
    root.right      = BinaryTreeNode(6)
    root.left.left  = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(5)
    root.right.right = BinaryTreeNode(7)
    print ("is tree BST:", isbst(root))
    print ("**if isBST = TRUE, then inorder traversal gives sorted list**")
    print ("\tfind kth smallest element in the BST:", find_kth_elements(root,3))
     
if __name__ == '__main__':
    main()
