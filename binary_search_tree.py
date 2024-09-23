class Node:
    def __init__(self, key):
        # Initialize a new node with a given key
        self.left = None  # Left child initialized to None
        self.right = None  # Right child initialized to None
        self.val = key  # Set the value of the node

class BinarySearchTree:
    def __init__(self):
        # Initialize an empty Binary Search Tree
        self.root = None  # Root of the BST is initialized to None

    def insert(self, key):
        # Insert a new key into the BST
        if self.root is None:
            # If the tree is empty, set the root to a new node with the key
            self.root = Node(key)
        else:
            # Otherwise, call the recursive insert method
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, current_node, key):
        # Helper method to insert a key recursively
        if key < current_node.val:
            # If the key is less than the current node's value, go left
            if current_node.left is None:
                # If there is no left child, add the new node here
                current_node.left = Node(key)
            else:
                # If there is a left child, recurse down the left subtree
                self._insert_recursively(current_node.left, key)
        else:
            # If the key is greater than or equal to the current node's value, go right
            if current_node.right is None:
                # If there is no right child, add the new node here
                current_node.right = Node(key)
            else:
                # If there is a right child, recurse down the right subtree
                self._insert_recursively(current_node.right, key)

    # Implement traversal methods
    def in_order_traversal(self, node):
        # In-order traversal (left, root, right)
        if node:
            self.in_order_traversal(node.left)  # Traverse left subtree
            print(node.val, end=' ')  # Visit current node
            self.in_order_traversal(node.right)  # Traverse right subtree

    def pre_order_traversal(self, node):
        # Pre-order traversal (root, left, right)
        if node:
            print(node.val, end=' ')  # Visit current node
            self.pre_order_traversal(node.left)  # Traverse left subtree
            self.pre_order_traversal(node.right)  # Traverse right subtree

    def post_order_traversal(self, node):
        # Post-order traversal (left, right, root)
        if node:
            self.post_order_traversal(node.left)  # Traverse left subtree
            self.post_order_traversal(node.right)  # Traverse right subtree
            print(node.val, end=' ')  # Visit current node

    def search(self, key):
        # Search for a key in the BST
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        # Helper method to search recursively
        if node is None or node.val == key:
            # Return the node if found or None if not found
            return node
        if key < node.val:
            # If the key is less than the current node's value, search in the left subtree
            return self._search_recursively(node.left, key)
        # If the key is greater, search in the right subtree
        return self._search_recursively(node.right, key)

if __name__ == "__main__":
    bst = BinarySearchTree()  # Create a new Binary Search Tree
    
    # Insert nodes into the BST
    bst.insert(7)
    bst.insert(3)
    bst.insert(9)
    bst.insert(1)
    bst.insert(5)

    print("In-order Traversal:")
    bst.in_order_traversal(bst.root)  # Perform in-order traversal
    print("\nPre-order Traversal:")
    bst.pre_order_traversal(bst.root)  # Perform pre-order traversal
    print("\nPost-order Traversal:")
    bst.post_order_traversal(bst.root)  # Perform post-order traversal

    # Search for a specific value in the BST
    search_value = 9
    found_node = bst.search(search_value)  # Search for the value
    if found_node:
        print(f"\nValue {search_value} found in the BST.")  # If found
    else:
        print(f"\nValue {search_value} not found in the BST.")  # If not found
