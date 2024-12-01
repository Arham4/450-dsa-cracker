def search(self, node, x):
    if not node:
        return 0
    if node.data == x:
        return 1
    return 1 if self.search_tree(node.left, x) or self.search_tree(node.right, x) else 0

def search_tree(self, node, x):
    if not node:
        return False
    if node.data == x:
        return True
    return self.search_tree(node.left, x) or self.search_tree(node.right, x)
