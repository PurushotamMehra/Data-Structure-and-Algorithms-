# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class linked_List:
#     def __init__(self):
#         self.head = None

#     def insertAtBeginning(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def insertEnd(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current_Node = self.head

#         while current_Node.next:
#             current_Node = current_Node.next

#         current_Node.next = new_node

#     def insertAtIndex(self, index, data):
#         new_node = Node(data)
#         current_node = self.head
#         pos = 0

#         if pos == index:
#             self.insertAtBeginning(data)
#         else:
#             while current_node is not None and pos + 1 != index:
#                 pos += 1
#                 current_node = current_node.next

#             if current_node is not None:
#                 new_node.next = current_node.next
#                 current_node.next = new_node
#             else:
#                 print("Index does not Exist")

#     def updateNode(self, index, val):
#         current_Node = self.head
#         position = 0

#         if position == index:
#             current_Node.data = val

#         else:
#             while current_Node is not None and position != index:
#                 position = position + 1
#                 current_Node = current_Node.next

#             if current_Node is not None:
#                 current_Node.data = val
#             else:
#                 print("Index Does Not exist")

#     def deleteFirstNode(self):
#         if self.head is None:
#             return
#         self.head = self.head.next

#     def deleteLastNode(self):
#         if self.head is None:
#             return

#         current_Node = self.head

#         while current_Node.next.next:
#             current_Node = current_Node.next

#         current_Node.next = None

#     def deleteAtIndex(self, index):
#         if self.head is None:
#             return

#         current_Node = self.head
#         position = 0

#         if position == index:
#             self.deleteFirstNode()

#         else:
#             while current_Node is not None and position + 1 != index:
#                 position += 1
#                 current_Node = current_Node.next

#             if current_Node is not None:
#                 current_Node.next = current_Node.next.next
#             else:
#                 print("Non Non Non index found")

#     def removeData(self, data):
#         current_node = self.head

#         while current_node is not None and current_node.next.data != data:
#             current_node = current_node.next

#         if current_node is None:
#             return
#         else:
#             current_node.next = current_node.next.next

#     def printingLL(self):
#         current_Node = self.head
#         ll_Str = ''
#         while current_Node:
#             ll_Str += str(current_Node.data) + '->'
#             current_Node = current_Node.next

#         print(ll_Str)

#     def getSize(self):
#         size = 0
#         if self.head:
#             current_Node = self.head
#             while current_Node:
#                 size += 1
#                 current_Node = current_Node.next

#             return size
#         else:
#             return 0



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertBeginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node 
            return
        else:
            node.next = self.head
            self.head = node 
            
    def insertEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        # position = 0
        
        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = node
                
    def insertAtIndex(self, data, index):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        position = 0
        
        if position == index:
            self.insertBeginning(data)
        else:
            while currentNode is not None and position + 1 != index:
                position = position + 1
                currentNode = currentNode.next
            if currentNode is not None:
                currentNode.next = node
            else:
                print("FuckYouITsNotPresent")
                
    
    def updatingNode(self, index, val):
        if self.head is None:
            return
    
        currentNode = self.head
        Position = 0
        
        if Position ==  index:
            currentNode.data = val
        
        else:
                    
            while currentNode is not None and Position != index:
                currentNode = currentNode.next
                Position += 1
                
            if currentNode is not None:
                currentNode.data = val
            else:
                print("Nai hai")
                
    def deleteBeginning(self):
        if self.head is None:
            return
        self.head = self.head.next
        
           
    def deleteEnd(self):
        if self.head is None:
            return

        currentNode = self.head
        
        while currentNode.next.next:
            currentNode = currentNode.next
            
        currentNode.next = None
         
        
    def deleteAtIndex(self, index):
        if self.head is None:
            return
        
        position = 0
        currentNode = self.head
        
        if position == index:
            self.deleteBeginning()
        else:
            while(currentNode is not None and position+1 != index):
                currentNode = currentNode.next
                position += 1
            if currentNode is not None:
                currentNode.next = currentNode.next.next
            else:
                print("nai hai")
        
                
    def removeWithData(self, data):
        currentNode = self.head
        while(currentNode.data is not None and currentNode.next.data != data):
            currentNode = currentNode.next
            
        if currentNode == None:
            return
        else:
            currentNode.next = currentNode.next.next
            
                
    def printingLL(self):
        currentNode = self.head
        llstr = ''
        
        while currentNode:
            llstr += str(currentNode.data) + '->'
            currentNode = currentNode.next
            
        print(llstr)

        
    def getSize(self):
        currentNode = self.head
        size = 0
        
        while currentNode:
            size += 1
            currentNode = currentNode.next
            
        return size

                 
        

LL = LinkedList()

LL.insertEnd('a')
LL.insertEnd('b')
LL.insertBeginning('c')
LL.insertEnd('d')
LL.insertAtIndex(2, 'g')
print(LL.getSize())

print("Linked List : ")
LL.printingLL()

print("\nRemove First Node : ")
LL.deleteBeginning()
LL.printingLL()

print("Remove Last Node : ")
LL.deleteEnd()
LL.printingLL()

print("Remove index 1 : ")
LL.deleteAtIndex(1)
LL.printingLL()

print("LinkedList after Methods")
LL.printingLL()

print("\nUpdate Node value")
LL.updatingNode(0, 'z')
LL.printingLL()

print("\nSize of Linked List : ")
print(LL.getSize())



   