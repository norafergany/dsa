from collections import deque


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def breadth_search(node):
    stack = deque()

    stack.append(node.left)
    stack.append(node.right)
    while stack:
        node = stack.popleft()
        print(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


my_tree = BinaryTreeNode(5)
left = my_tree.insert_left(8)
right = my_tree.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
right.insert_right(4)


breadth_search(my_tree)
