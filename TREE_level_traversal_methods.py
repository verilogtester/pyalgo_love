# Python program to for tree level based traversals (BFS) 
# (This is Iterative Approach)
from asyncio.queues import Queue
 
# A class that represents an individual node in a 
# Binary Tree 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
    def getData(self):
        return self.val
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

# A function to do inorder tree levels traversal (BFS) 
#
def iter_printLevelorder(root): 
    if root == None:
        return
    result = []
    q = [root] # Queue 
    
    while q: # as long as queue is not empty
        v = q.pop(0)
        result.append(v.val)
        if v.left is not None:
            q.append(v.left)
            
        if v.right is not None:
            q.append(v.right)
    print ("Iterative appraoch Level traversal - queue data type", result)
    
    
import queue
def iter_printLevelorder_queue(root): 
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    node = None
    result = []
    while not q.empty():
        node = q.get() # Dequeue FIFO
        result.append(node.getData())
        if node.getLeft() is not None:
            q.put(node.getLeft())
        if node.getRight() is not None: 
            q.put(node.getRight())
      
    print ("Iterative appraoch Level traversal - queue module used", result)
  
     
            
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
Level order traversal of binary tree is
Iterative appraoch Level traversal - queue data type [1, 2, 3, 4, 5]
Iterative appraoch Level traversal - queue module used [1, 2, 3, 4, 5]  
'''
print ("Level order traversal of binary tree is")
iter_printLevelorder(root)

iter_printLevelorder_queue(root)
