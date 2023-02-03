import math
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


my_tree = BinaryTreeNode(1)
right = my_tree.insert_right(2)
right_right = right.insert_right(3)
right_right.insert_right(4)


def is_balanced(tree_root):
    # Determine if the tree is superbalanced
    # print(tree_root.)

    if not tree_root:
        return True
    count = -1
    leaf_count = 0
    stack = [(tree_root, count)]
    initial_depth = 0
    initial_found = False
    comp_found = False
    none_found = False
    none_count = 0
    while stack:
        tree_root, depth = stack.pop()
        print(tree_root, depth)
        depth += 1
        if tree_root:
            print(tree_root.value, depth)
            # count += 1
            # if tree_root.right:
            stack.append((tree_root.right, depth))
            if not tree_root.right and not tree_root.left:
                none_found = True
            # if tree_root.left:
            stack.append((tree_root.left, depth))

        if not tree_root:
            # if tree_root == last_val:
            #     return True
            # if none_found:
            #     return True
            if not initial_found:
                initial_found = True
                initial_depth = depth
                comp_depth = initial_depth
                leaf_count += 1
                print("depths: ", initial_depth, comp_depth)
                continue
            if initial_found and not comp_found:
                leaf_count += 1
                comp_found = True
                comp_depth = depth
                if abs(comp_depth - initial_depth) > 1:
                    print("x")
                    return False
                if comp_depth > initial_depth:
                    max_depth = comp_depth
                    min_depth = initial_depth
                elif comp_depth < initial_depth:
                    max_depth = initial_depth
                    min_depth = comp_depth
                else:
                    min_depth = max_depth = initial_depth = comp_depth
                continue
            if comp_found:
                if max_depth != min_depth:
                    print(max_depth, min_depth)
                    print(tree_root.value, depth)
                    if depth > max_depth or depth < min_depth:
                        print("y")
                        return False
                elif max_depth == min_depth:
                    if abs(depth - max_depth) > 1 or abs(depth - min_depth) > 1:
                        print("z")
                        return False
                    else:
                        max_depth = max(depth, max_depth)
                        min_depth = min(depth, min_depth)
        last_val = tree_root

    return True


print(is_balanced(my_tree))
# more_right.insert_right(7)

# def dfs(node):
#     if not node:
#         return True
#     count = -1
#     leaf_count = 0
#     stack = [(node, count)]
#     initial_depth = 0
#     initial_found = False
#     comp_found = False
#     while stack:
#         node, depth = stack.pop()
#         depth += 1
#         if node:
#             print(node.value, depth)
#             # count += 1
#             stack.append((node.right, depth))
#             stack.append((node.left, depth))
#         if not node:
#             initial_found = True
#             initial_depth = depth
#             comp_depth = initial_depth
#             leaf_count += 1
#             if initial_found:
#                 leaf_count += 1
#                 continue
#             if leaf_count == 2 and not comp_found:
#                 comp_depth = depth
#                 comp_found = True
#                 if abs(comp_depth - initial_depth) > 1:
#                     return False
#                 if comp_depth > initial_depth:
#                     max_depth = comp_depth
#                     min_depth = initial_depth
#                 elif comp_depth < initial_depth:
#                     max_depth = initial_depth
#                     min_depth = comp_depth
#                 else:
#                     initial_depth = comp_depth = min_depth = max_depth
#                 continue
#             else:
#                 if max_depth != min_depth:
#                     if depth > max_depth or depth < min_depth:
#                         return False
#                 elif max_depth == min_depth:
#                     if abs(depth - max_depth) > 1 or abs(depth - min_depth) > 1:
#                         return False
#                     else:
#                         max_depth = max(depth, max_depth)
#                         min_depth = min(depth, min_depth)
#     return True
#
#
# result = dfs(my_tree)
# print(result)


# def is_balanced(tree_root):
#     # Determine if the tree is superbalanced
#     # print(tree_root.)
#
#     stack = deque()
#     initial_depth = 0
#     next_depth = 0
#     min_depth = -math.inf
#     max_depth = math.inf
#
#     stack.append(tree_root.left)
#     # initial_depth += 1
#     stack.append(tree_root.right)
#     # next_depth += 1
#     comps_set = False
#     initial_set = False
#
#     while stack:
#         tree_root = stack.popleft()
#         # print(tree_root.value)
#         # if node == stack[0]:
#         #     current_depth += 1
#
#         # if hasattr(tree_root, 'data'):
#         #     print("test ", tree_root.data)
#         if tree_root:
#             if tree_root.left:
#                 stack.append(tree_root.left)
#                 initial_depth += 1
#             if tree_root.right:
#                 stack.append(tree_root.right)
#                 next_depth += 1
#             if not tree_root.left and not tree_root.right and not initial_set:
#
#             if not tree_root.left and not tree_root.right and not comps_set:
#                 # its a leaf
#                 if initial_depth == 0 or next_depth == 0:
#                     if initial_depth == 0:
#                         min_depth = max_depth = next_depth
#                     elif next_depth == 0:
#                         min_depth = max_depth = initial_depth
#                 else:
#                     min_depth = min(initial_depth, next_depth)
#                     max_depth = max(initial_depth, next_depth)
#                 # print(min_depth, max_depth)
#                 if (max_depth - min_depth) > 1:
#                     return False
#                 comps_set = True
#                 # initial_depth = 0
#                 # next_depth = 0
#                 continue
#             elif not tree_root.left and not tree_root.right:
#                 print(initial_depth, next_depth)
#                 print(max_depth, min_depth)
#                 if initial_depth != 0 or next_depth != 0:
#                     if abs(initial_depth - next_depth) > 1:
#                         print("false")
#                         return False
#                 if (abs(initial_depth - min_depth) > 1 or abs(initial_depth - max_depth) > 1) and (
#                         abs(next_depth - min_depth) > 1 or abs(next_depth - max_depth) > 1) and (
#                         initial_depth != 0 or next_depth != 0):
#                     return False
#     return True
