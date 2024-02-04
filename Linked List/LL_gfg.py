class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.next = None
        
    def insert_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node
            
    def InsertAtIndex(self, index, data):
            node = Node(data)
            current_Node = self.head
            pos = 0
            
            if pos == index:
                self.insert_begin(data)
            else:
                while(current_Node != None and pos+1 != index):
                    pos = pos+1
                    current_Node = current_Node.next
                    
                if current_Node != None:
                    node.next = current_Node.next
                    current_Node.next = node
                else:
                    print("Not Present")
                    
    def insertAtEnd(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            return
        
        cur_node = self.head
        while(cur_node.next):
            cur_node = cur_node.next
            
        cur_node.next = Node
        
    # def updateNode(self, index, data):
        