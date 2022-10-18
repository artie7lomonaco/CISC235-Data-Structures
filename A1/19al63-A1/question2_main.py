from stack import *

#main function for testing code
def main():
    #tests on the array stack
    stack = Stack()
    print("For Array-based list stack")
    print("Stack is empty: ", stack.is_empty())
    stack.push(1)
    stack.push(3)
    stack.push(7)
    print("Top of stack: ", stack.top())
    print("Stack is empty: ", stack.is_empty())
    print("Size of stack: ", stack.size())
    stack.pop()
    stack.pop()
    stack.pop()
    print("Stack is empty: ", stack.is_empty())
    print("-------------------------------------------------")

    #tests on the linked stack
    stack2 = LinkedStack()
    print("For linked stack")
    print("Stack is empty: ", stack2.is_empty())
    stack2.push(1)
    stack2.push(3)
    stack2.push(7)
    print("Top of stack: ", stack2.top())
    print("Stack is empty: ", stack2.is_empty())
    print("Size of stack: ", stack2.size())
    stack2.pop()
    stack2.pop()
    stack2.pop()
    print("Stack is empty: ", stack2.is_empty())

main()
