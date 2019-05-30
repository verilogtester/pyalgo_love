#Doubly Linked list example 
#benefits
#	# Can iterate the list in either direction
#	# Can delete a node without iterating through the list (if given pointer to the node)
 
# the Node Class
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
 
    def get_prev(self):
        return self.prev
    
    def set_prev(self, prev):
        self.prev = prev
 
#the LinkedList class
 
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        if self.head:
            self.head.set_prev(new_node)
        self.head = new_node
        self.count += 1
        
    def dump_list(self):
        tempnode = self.head
        while tempnode:
            print ("Node: ",tempnode.get_data())
            tempnode = tempnode.get_next()
 
    def find(self, data):
        item = self.head
 
        while (item != None):
            if item.get_data() == data:
                return data,'exist in the list'
            else:
                item = item.get_next()
        return data, 'Not Existing' 
 
    def deleteAt(self, idx):
        this_node = self.head
        prev_node = None
        if idx > self.count:
            return
        if self.head == None:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempidx = 0
            this_node = self.head
            while this_node:
                if tempidx == idx:
                    next = this_node.get_next()
                    prev = this_node.get_prev()
                    if next:
                        next.set_prev(prev)
                    if prev:
                        prev.set_next(next)
                    else:
                        self.head = this_node
                    self.count -= 1
                    return True # data removed
                else:
                    this_node = this_node.get_next()
                tempidx += 1
            return False
            
        self.count -= 1
            
    def remove(self, data):
        this_node = self.head
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                next = this_node.get_next()
                prev = this_node.get_prev()
                
                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
                else:
                    self.head = this_node
                self.count -= 1
                return True # data removed
            else: #increment the pointer 
                this_node = this_node.get_next()
        return False
               
                            
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(31)
itemlist.insert(232)
itemlist.insert(50)
print ("Find operation", itemlist.find(38))
print ("Find operation", itemlist.find(381))
itemlist.dump_list()
print("Item count:", itemlist.get_count())
itemlist.deleteAt(3)
print ("delete operation", itemlist.remove(31))
print("Item count:", itemlist.get_count())
itemlist.dump_list()
