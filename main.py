from splay_tree import *
from random import shuffle


# key_node = [_ for _ in range(10)]
# #
splay_tree = SplayTree()
# shuffle(key_node)
key_node = [3, 2, 0, 1, 6, 5, 4, 7, 8, 9]
for key in key_node:
    splay_tree.insert(key)

splay_tree.pre_order(splay_tree.root)
print("-".center(10, "-"))
key = 4
root = splay_tree.root
if splay_tree.search(4) is not None:
    # splay_tree.find(4)
    splay_tree.pre_order(splay_tree.root)
