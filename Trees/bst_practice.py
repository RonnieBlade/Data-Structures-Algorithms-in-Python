class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insertToNode(self.root, new_val)


    def insertToNode(self, node, new_val):
        if node is None:
            return Node(new_val)
        elif new_val < node.value:
            node.left = self.insertToNode(node.left, new_val)
        else:
            node.right = self.insertToNode(node.right, new_val)
        return node

    def search(self, find_val):
        return self.searchInNode(self.root, find_val)

    def searchInNode(self, node, find_val):
        if node is None:
            return False
        if node.value == find_val:
            return True
        if find_val < node.value:
            return self.searchInNode(node.left, find_val)
        else:
            return self.searchInNode(node.right, find_val)



# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))