import math
from collections import deque

"""
there are most 2 depths and theyre at most 1 apart
traverse the tree until you get to a leaf, keeping track of the depth --> set initial depth to that 
traverse until you get to the next leaf, keeping track of the depth 
     if that depth is bigger by 1: its the new max
     if that depth is smaller by 1 : its the new min
     otherwise: return false 

there are most 2 depths and theyre at most 1 apart
traverse the tree until you get to the first leaf --> thats the initial_depth
until you get another leaf, initial_depth == comp_depth
when you get to the 2nd leaf, check if its diff from initial_depth > 1:
    - diff greater than 1--> return false
    - equal to initial_depth, still no comp
    - greater by 1: its the upper boundary
    - less by 1: its the lower boundary
traverse the rest of the tree, at each node, check the depth against initial_depth and comp_depth



"""
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
    initial_depth = 0
    next_depth = 0
    min_depth = -math.inf
    max_depth = math.inf

    stack.append(node.left)
    # initial_depth += 1
    stack.append(node.right)
    # next_depth += 1
    comps_set = False
    while stack:
        node = stack.popleft()
        print(node.value)
        # if node == stack[0]:
        #     current_depth += 1
        if node.left:
            stack.append(node.left)
            initial_depth += 1
        if node.right:
            stack.append(node.right)
            next_depth += 1
        if not node.left and not node.right and not comps_set:
            # its a leaf
            min_depth = min(initial_depth, next_depth)
            max_depth = max(initial_depth, next_depth)
            print(min_depth, max_depth)
            if (max_depth - min_depth) > 1:
                return False
            comps_set = True
            # initial_depth = 0
            # next_depth = 0
            continue
        elif not node.left and not node.right:
            print(initial_depth, next_depth)
            if initial_depth < min_depth or initial_depth > max_depth or next_depth < min_depth or next_depth > max_depth:

                return False
    return True


my_tree = BinaryTreeNode(5)
left = my_tree.insert_left(8)
right = my_tree.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
more_right = right.insert_right(4)
more_right.insert_right(7)


print(breadth_search(my_tree))
