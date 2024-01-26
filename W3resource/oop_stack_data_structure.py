# Exercise:
# Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.

# Info: Stack is a linear data structure with a particular order for it's operations.
# The order may be LIFO (Last in first out) or FILO (First in last out).
# LIFO: Element that was inserted last comes out first.

class Stack:
    def __init__(self):
        self.my_stack = []

# Define the push method to insert an item into the stack.
    def push(self, last_item):
        self.my_stack.append(last_item)
        return self.my_stack

# Define the pop method to remove the last added item from the stack.
    def pop(self):
        if len(self.my_stack) == 0:
            return "The stack is already empty."
        else:
            last_item = self.my_stack[len(self.my_stack) - 1]
            self.my_stack.remove(last_item)
            return self.my_stack


#Example usage:
# Create an instance from the Stack class
stack = Stack()

# Apply the push method three times on the stack object to add three items to the stack.
first_item_in = stack.push("a")
second_item_in = stack.push("b")
last_item_in = stack.push("c")
print(last_item_in)

#Apply the pop method to remove the last added item from the stack.
last_item_first_out1 = stack.pop()
print(last_item_first_out1)

last_item_first_out2 = stack.pop()
print(last_item_first_out2)

last_item_first_out3 = stack.pop()
print(last_item_first_out3)

last_item_first_out4 = stack.pop()
print(last_item_first_out4)

