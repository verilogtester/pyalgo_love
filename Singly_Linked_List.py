#Linked list example
 
# the Node Class
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
 
 
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
        if idx > self.count:
            return
        if self.head == None:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempidx = 0
            node = self.head
            while tempidx < idx -1:
                node = node.get_next()
                tempidx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
            
    def remove(self, data):
        
        this_node = self.head
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node: # jump the pointer to remove element
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node
                self.count -= 1
                return True
            else: #increment the pointer 
                prev_node = this_node
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
itemlist.deleteAt(1)
print ("delete operation", itemlist.remove(31))
print("Item count:", itemlist.get_count())
itemlist.dump_list()
