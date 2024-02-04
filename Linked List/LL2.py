# class Node:
#     def __init__(self, data = None, next = None):
#         self.data = data
#         self.next = next
        
# class LinkedList:
#     def __init__(self):
#         self.head = None
        
#     def insert_at_beginning(self, data):
#         node = Node(data, self.head)
#         self.head = node
        
#     def insert_at_the_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
        
#         itr = self.head
        
#         while itr.next:
#             itr = itr.next
            
#         itr.next = Node(data, None)
            
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_the_end(data)
    
#     def get_length(self):
#         count = 0
#         itr = self.head
        
#         while itr:
#             count += 1
#             itr = itr.next
            
#         return count
        
        
#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.head = self.head.next
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break

#             itr = itr.next
#             count+=1
         
#     def insert_at(self, index, data):
#         if index < 0 or index>= self.get_length():
#             raise Exception("You fucking Dumbass bitch")
        
#         if index == 0:
#             self.insert_at_beginning(data)
        
#         count = 0
#         itr = self.head
        
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
                
#             itr = itr.next
#             count += 1
                                    
#     def print(self):
#         if self.head is None:
#             print("The Linked List is empty : ")
#             return
            
#         itr = self.head
#         ll_str = ''
#         while itr:
#             ll_str += str(itr.data) + '->'
#             itr = itr.next
                
#         print(ll_str)  # Print ll_str after the loop
    
    
    
# if __name__ == "__main__":
#     ll = LinkedList()
#     print()
#     ll.insert_values([34, 67, 89, 23, 11])
#     print("Inserting values : ")
#     ll.print()
#     print()

#     ll.insert_at_beginning(21)
#     print("Inserting at the Beginning : ")
#     ll.print()
#     print()

#     ll.insert_at_the_end(99)
#     print("Inserting at the End : ")
#     ll.print()
#     print()
    
#     # ll.get_length()
#     ll.remove_at(3)
#     ll.print()




class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __inti__(self):
        self.head = None
        
    def get_length(self):
        count = 0
        itr = self.head
        
        while itr:
            count += 1
            itr = itr.next
            
        return count
        
    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
            
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def print(self):
        if self.head is None:
            print("List emptier than yo love life")
            return
            
        itr = self.head
        ll_str = ''
        
        while itr:
            ll_str += str(itr.data) + '->'  
            itr = itr.next
            
        return ll_str
    
    def insert_vales(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)
            
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
            
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node 
                break
            itr = itr.next
            count += 1
            
    def remove_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Fuck off")
        
        if index == 0:
            self.head = self.head.next
            return
        
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
             
    