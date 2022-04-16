class Node:
    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"node[{self.key}]"


class SplayTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key, parent=None):
        if parent is None:
            parent = self.root
        # если корень, нулевой то создаем новый узел
        if self.root is None:
            self.root = Node(key)
            return True
        elif key < parent.key:
            if parent.left is None:
                parent.left = Node(key)
                return True
            else:
                self.insert(key, parent.left)
        else:
            if parent.right is None:
                parent.right = Node(key)
                return True
            else:
                self.insert(key, parent.right)

    # прямой проход дерева
    @staticmethod
    def pre_order(root_: Node):
        if root_ is not None:
            print(f"parent: {root_}, leftChild: {root_.left}, RightChild: {root_.right}")
            SplayTree.pre_order(root_.left)
            SplayTree.pre_order(root_.right)

    def search(self, key, node=None, parent=None, g=None, gg=None):
        """Find if a keyue is in the tree. Takes one argument
        (the keyue to find). If the keyue is in the tree, returns
        the node object. Otherwise returns None."""
        if node is None:
            node = self.root
        if node is None:
            # obviously it's not in an empty tree
            return None
        elif key == node.key:
            # If it's found, we need to move things around
            if parent is not None:
                if g is None:
                    # Zig: swap node with its parent
                    self.rotate(node, parent, g)
                elif ((g.left == parent and parent.left == node) or
                      (g.right == parent and parent.right == node)):
                    # Zig-zig: swap parent with grandparent
                    self.rotate(parent, g, gg)
                    # Then swap node with parent
                    self.rotate(node, parent, gg)
                else:
                    # Zig-zag: swap node with parent
                    # получается делается zig с родителем
                    self.rotate(node, parent, g)
                    # Then swap node with grandparent
                    # делается zag
                    self.rotate(node, g, gg)
            # return node - после этого момента выводиться значение
            # но нам нужно производить поиск до корня
            if self.root.key == key:
                return True
            self.search(key)

        if self.root.key == key:
            return True
        # с помощью этих функций мы пробегаемся по дереву
        elif key < node.key:
            # Search left
            if node.left is not None:
                # self.search(key, node.left, node, parent, g)
                leftrv = self.search(key, node.left, node, parent, g)
                if leftrv is not None:
                    return leftrv
        elif key > node.key:
            if node.right is not None:
                # self.search(key, node.right, node, parent, g)
                rightrv = self.search(key, node.right, node, parent, g)
                if rightrv is not None:
                    return rightrv
        return None

    def rotate(self, node, parent, grand_parent=None):
        """Swap a node with its parent, keeping all child nodes
        (and grandparent node) in order."""
        # zig - right rotate
        if node == parent.left:
            parent.left = node.right
            node.right = parent
            if self.root == parent:
                self.root = node
        # zag - left rotate
        elif node == parent.right:
            parent.right = node.left
            node.left = parent
            if self.root == parent:
                self.root = node

        if grand_parent is not None:
            if grand_parent.right == parent:
                grand_parent.right = node
            elif grand_parent.left == parent:
                grand_parent.left = node
