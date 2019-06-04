""" Tree - Abstracted Data Structure like linked list. 
Tree has branches (2 or many)

Binary tree is one type of tree

Binary Tree 		|	Heap
    Linked LIst		|	-> List and Array
        (Node)		|
        -> Left		|
        -> Right	|

Note - Always make sure to keep the head intact, to know the
starting point 

Tree Traversal:
    1) In-order Traversal
        L -> ROOT Node -> R
    2) pre-order Traversal
        ROOT Node -> L -> R
    3) Post-order Traversal
        L -> R -> ROOT Node
    4) Level Order Traversal
        L1 -> L2 -> L3 (BFS)
        -------------->
        
Traversal
"""

# Python program to for tree traversals (This is recursive Approach)
  
# A class that represents an individual node in a 
# Binary Tree 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
  
# A function to do inorder tree traversal 
def printInorder(root): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left) 
  
        # then print the data of node 
        print(root.val), 
  
        # now recur on right child 
        printInorder(root.right) 
  
  
  
# A function to do postorder tree traversal 
def printPostorder(root): 
  
    if root: 
  
        # First recur on left child 
        printPostorder(root.left) 
  
        # the recur on right child 
        printPostorder(root.right) 
  
        # now print the data of node 
        print(root.val), 
  
  
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right) 
  
  
# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 

'''
		1(ROOT)
     2		3
  4		5
'''
print ("Preorder traversal of binary tree is")
printPreorder(root) 
  
print ("\nInorder traversal of binary tree is")
printInorder(root) 
  
print ("\nPostorder traversal of binary tree is")
printPostorder(root) 
