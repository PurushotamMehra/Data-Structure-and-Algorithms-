class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None) 
         
    def print_LL(self):
        if self.head is None:
            print("This Bitch Empty")
            return
        
        itr = self.head
        ll_str = ''
        
        while itr:
            ll_str += str(itr.data) + '->'
            itr = itr.next
            
        print(ll_str)
        
    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)             
            
    def get_length(self):
        count = 0
        itr = self.head
        
        while itr:
            count += 1
            itr = itr.next
            
        return count

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("invalid Index")
            
        
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
        
    def add_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1
         
    def sort_list(self):
        sort_list = []
        
        itr = self.head
        
        while itr:
            sort_list.append(itr.data)
            itr = itr.next
        
        sort_list.sort()
        return sort_list

        
        
if __name__ == '__main__':
    
    LL = LinkedList()

    LL.insert_list([13,78,27,9])
    LL.insert_at_beginning(5)

    print(LL.get_length())
    # LL.remove_at(93)
    LL.add_at(12, 4)

    LL.print_LL()
    
    
    temp = LL.sort_list()
    print(temp)
    
    
    
        
        