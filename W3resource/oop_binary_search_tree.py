# Exercise: 
# Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.

# Info: A binary search tree (BST) has a root node with a value. This root node may have child nodes that can be trees themselves.
# Going to the left of the root node the next value has to be smaller, on the right side the value is equal or bigger.

# Create the class Tree to represent a binary search tree.
class Tree:
    # Create a basic constructor to initialize the binary search tree (BST) with an empty root node.
    def __init__(self, value):
        self.value = value
        # Child node will be initialized with None:
        self.left = None
        self.right = None


# Create an insert method to enter a value into the BST so that the value ends up in the right place.
    def insert(self, child_value):
        if child_value < self.value:
            if self.left is None:
                # If the value is None, self.left becomes a new node with a new value.
                self.left = Tree(child_value)
            else:
                # If self.left has already a value assigned (a new node),
                # then the insert method needs to be applied with the same value onto that node.
                self.left.insert(child_value)
        else:
            if self.right is None:
                self.right = Tree(child_value)
            else:
                self.right.insert(child_value)
           

# Define a search method to recursively search for elements in the binary search tree and return the node if found.
    def search(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(value) 
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.search(value) 
        else: 
            # If the searched value is equal to the actual value return True.
            return True
 

# Example usage: 
# Create an instance of Tree.
tree = Tree(8)

# Insert values into the BST.
tree.insert(6)
tree.insert(9)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(1)
tree.insert(2)
tree.insert(14)
tree.insert(13)
tree.insert(6)

# Print the values 6 and 2 of the given nodes.
print(tree.left.right.value)
print(tree.left.left.left.left.left.right.value)

# Search for the existing value 14 and the non-existing value 10 in the BST.
print(tree.search(14))
print(tree.search(10))

