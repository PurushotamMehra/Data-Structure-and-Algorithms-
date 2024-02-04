# ********** COMPLETE TREE TUTORIAL WITH PYTHON ********** 
# 1. Defining a Tree
# 2. Adding a Node
# Building up a Tree
# Printing all nodes Inorder
# Printing all Nodes PostOrder
# Printing all Nodes PreOrder
#Breadth-First Search (BFS) - Algorithm Using Queues
# BFS Python Code
# Depth-First Search (DFS) - Algorithm Using Stacks
# DFS Python Code
# Searching for a key in a Tree
#Exercise - Tree Top View
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        
    
def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end = ' ')
        inOrderPrint(r.right)

def preOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end = ' ')
        preOrderPrint(r.left)
        preOrderPrint(r.right)

    
def postOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end = ' ')
        postOrderPrint(r.right)
        postOrderPrint(r.left)
        
if __name__ == '__main__':
    root = Node('g')
    root.insert('c') 
    root.insert('b') 
    root.insert('a') 
    root.insert('e') 
    root.insert('d') 
    root.insert('f') 
    root.insert('i') 
    root.insert('h') 
    root.insert('j') 
    root.insert('k') 
    
print("=========================inOrderPrint============================")    
inOrderPrint(root)
print("\n=========================preOrderPrint===========================")
preOrderPrint(root)
print("\n=========================postOrderPrint==========================")
postOrderPrint(root)
                
                    
