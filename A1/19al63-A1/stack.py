#array stack implementaion
class Stack:
    #initialization class, with just a list called stack
    def __init__(self):
        self.stack = []

    #check if stack is empty
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    #pushes value v to top of stack, returns true as well
    def push(self, v):
        self.stack.append(v)
        return True

    #pops top element of stack, returns true if able to pop
    #return false if stack is empty, so could not pop
    def pop(self):
        if not self.is_empty():
            del self.stack[-1]
            return True
        return False

    #gets top of stack, returns end of list
    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    #size of stack, by size of list
    def size(self):
        return len(self.stack)


#first, creates node, which stores value of stack, and next
class Node:
    def __init__(self, v):
        self.v = v
        self.next = None

#linked list implementation of stack
class LinkedStack:
    def __init__(self):
        self.head = Node("head")
        self.s = 0

    #returns size of stack
    def size(self):
        return self.s

    #checks if stack is empty, returns true or false
    def is_empty(self):
        return self.s == 0

    # Get the top value of the stack
    def top(self):
        if not self.is_empty():
            return self.head.next.v

    # Push a value into the stack.
    def push(self, v):
        node = Node(v)
        node.next = self.head.next
        self.head.next = node
        self.s += 1

    # Remove top value from the stack and return removed value
    def pop(self):
        if not self.is_empty():
            remove = self.head.next
            self.head.next = self.head.next.next
            self.s -= 1
            return remove.v
