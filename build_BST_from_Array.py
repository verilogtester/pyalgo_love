""" Given a sorted array, convert an array into BST"""

class Node:
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


def build_bst(l):
    if len(l) == 0:
        return
    mid = len(l)//2 # integer division
    newNode = Node(l[mid])
    newNode.left  = build_bst(l[:mid])
    newNode.right = build_bst(l[mid+1:])
    return newNode

# A function to do inorder tree traversal 
def printInorder(root): 
    if root: 
        # First recur on left child 
        printInorder(root.left) 
        # then print the data of node 
        print(root.data), 
        # now recur on right child 
        printInorder(root.right) 

# A function to do preorder tree traversal 
def printPreorder(root): 
    if root: 
        # First print the data of node 
        print(root.data), 
        # Then recur on left child 
        printPreorder(root.left) 
        # Finally recur on right child 
        printPreorder(root.right)   

if __name__ == '__main__':
    #create the sample BST
    l = [1,3,5,7,9,11,13,16,19,21,25]
    print("\n creating BST")
    root = build_bst(l)
    print ("print Inorder BST")
    printInorder(root) # inorder traversal shows sorted binary search tree 
    print ("print PreOrder BST")
    printPreorder(root) # inorder traversal shows sorted binary search tree 
     


            
