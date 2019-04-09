class BinaryTree:

    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert_left(self, key):
        if self.left_child:
            new_node = BinaryTree(key)
            new_node.left_child = self.left_child
            self.left_child = new_node
        else:
            self.left_child = BinaryTree(key)
        return self.left_child

    def insert_right(self, key):
        if self.right_child:
            new_node = BinaryTree(key)
            new_node.right_child = self.right_child
            self.right_child = new_node
        else:
            self.right_child = BinaryTree(key)
        return self.right_child

    def set_left_child(self, node):
        self.left_child = node
        return node

    def set_right_child(self, node):
        self.right_child = node
        return node

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key
        return self


def construct():
    a = BinaryTree('a')
    b = BinaryTree('b')
    c = BinaryTree('c')
    d = BinaryTree('d')
    e = BinaryTree('e')
    f = BinaryTree('f')

    a.set_left_child(b)
    a.set_right_child(c)
    b.set_left_child(d)
    b.set_right_child(e)
    c.set_left_child(f)
    return a


# 前序遍历
def NLR(node):
    if not node:
        return
    print(node.key, end=' ')
    if node.left_child:
        NLR(node.left_child)
    if node.right_child:
        NLR(node.right_child)


# 中序遍历
def LNR(node):
    if not node:
        return
    if node.left_child:
        LNR(node.left_child)
    print(node.key, end=' ')
    if node.right_child:
        LNR(node.right_child)


# 后序遍历
def LRN(node):
    if not node:
        return
    if node.left_child:
        LNR(node.left_child)
    if node.right_child:
        LNR(node.right_child)
    print(node.key, end=' ')


if __name__ == '__main__':
    binary_tree = construct()
    NLR(binary_tree)
    print()
    LNR(binary_tree)
    print()
    LRN(binary_tree)
