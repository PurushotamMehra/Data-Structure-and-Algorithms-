# stack = []
# top = None

# def isEmpty(stack):
#     if stack == []:
#         return True
#     else: 
#         return False
    
# def stack_push(stack, item):
#     stack.append(item)
#     global top
#     top = len(stack) - 1
    
# def stack_pop(stack):
#     if isEmpty(stack):
#         return("Underflow")
#     else:
#         global top
#         i = stack.pop()
#         if len(stack) == 0:
#             top = None
#         else:
#             top = top -1
            
#     return i
        
# def peek(stack):
#     if isEmpty(stack):
#         return("Underflow")
#     else:
#         top = len(stack) - 1
#         return stack[top]
    
# def display(stack):
#     if isEmpty(stack):
#         print("Stack is Empty")
#     else:
#         top = len(stack) - 1
#         print(f"{stack[top]} <-- TOP")
#         for i in range(top - 1, -1, -1):
#             print(stack[i])
        
# print("STACK IMPLEMENTATION")
# stack_push(stack,12)
# stack_push(stack,9)
# stack_push(stack,42)
# stack_push(stack,69)
# stack_pop(stack)

# display(stack)

# print("\n")

# print(peek(stack))




class Stack:
    def __init__(self):
        self.stack = []
        self.top = None 
        
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False
        
    def stack_push(self, item):
        self.stack.append(item)
        self.top = len(self.stack) - 1
        
    def stack_pop(self):
        if self.isEmpty():
            print("Underflow")
        else:
            self.stack.pop()
            if len(self.stack) == 0:
                self.top = None
            else:
                self.top = self.top - 1
    
    def peek(self):
        if self.isEmpty():
            return "Underflow"
        else:
            top = len(self.stack) - 1
            return(self.stack[top])
        
    def display(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            self.top = len(self.stack) - 1
            print(f"{self.stack[self.top]} <-- Top")
            for i in range(self.
                           top - 1, -1, -1):
                print(self.stack[i])
     
Stack_ = Stack()
print("STACK IMPLEMENTATION")
Stack_.stack_push(12)
Stack_.stack_push(9)
Stack_.stack_push(42)
Stack_.stack_push(69)


Stack_.display()

print("\n")
Stack_.stack_pop()
Stack_.display()

print("\n")
print(Stack_.peek())