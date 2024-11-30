import collections

def LeftView(self, root):
    level = 1
    queue = collections.deque([(root, level)])
    left_view = []
    while queue:
        node, curr_level = queue.popleft()
        if not node:
            break
        if curr_level > len(left_view):
            left_view.append(node.data)
        if node.left:
            queue.append((node.left, curr_level + 1))
        if node.right:
            queue.append((node.right, curr_level + 1))
    return left_view
