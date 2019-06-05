# Python program to for tree traversals (This is generative Approach)
  
# A class that represents an individual node in a 
# Binary Tree 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

# A function to do inorder tree traversal 
def gen_printInorder(root): 
  
    if root: 
  
        # Then recur on left child 
        yield from gen_printInorder(root.left) 
        # First print the data of node 
        yield (root)  
        # Finally recur on right child 
        yield from gen_printInorder(root.right) 
    
  
# A function to do preorder tree traversal 
def gen_printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        yield (root)
  
        # Then recur on left child 
        yield from gen_printPreorder(root.left) 
  
        # Finally recur on right child 
        yield from gen_printPreorder(root.right) 
   
  
# A function to do postorder tree traversal 
def gen_printPostorder(root):
    if root == None:
        return  
    # First recur on left child 
    yield from gen_printPostorder(root.left) 
  
    # the recur on right child 
    yield from gen_printPostorder(root.right) 
  
    # now print the data of node 
    yield (root)
    
     
    

  
# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 

'''
        1(ROOT)
     2        3
  4        5
'''
print ("Preorder traversal of binary tree is")
for items1 in gen_printPreorder(root):
    print (items1.val)  

print ("\nInorder traversal of binary tree is")
for items2 in gen_printInorder(root):
    print (items2.val)   

print ("\nPostorder traversal of binary tree is")
for items3 in gen_printPostorder(root):
    print (items3.val)  
