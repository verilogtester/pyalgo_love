# Python program to for tree traversals (This is Iterative Approach)
 
# A class that represents an individual node in a 
# Binary Tree 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

# A function to do inorder tree traversal 
#
def iter_printInorder(root): 
    if root == None:
        return
    result = []
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.val)
            node = node.right
    print (result)
# A function to do preorder tree traversal
# The nodes values are appended to the result list in traversal order 
def iter_printPreorder(root): 
    if root is None:
        return
    result = []
    stack = []
    stack.append(root)
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    print (result)
# A function to do postorder tree traversal 
# each node is visited twice. we use a previous variable to keep track 
# of the earlier traversed node 
def iter_printPostorder(root):
    if root == None:
        return 
    
    result = []
    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.val)
                node = None
    print (result)
# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 

'''
Input:
        1(ROOT)
     2        3
  4        5
  
Output:
Preorder traversal of binary tree is
[1, 2, 4, 5, 3]

Inorder traversal of binary tree is
[4, 2, 5, 1, 3]

Postorder traversal of binary tree is
[4, 5, 2, 3, 1]
'''
print ("Preorder traversal of binary tree is")
iter_printPreorder(root)

print ("\nInorder traversal of binary tree is")
iter_printInorder(root)  

print ("\nPostorder traversal of binary tree is")
iter_printPostorder(root)
