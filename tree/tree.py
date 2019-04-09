class Tree:

    def __init__(self, key):
        self.key = key
        self.children = []

    def set_key(self, key):
        self.key = key
        return self

    def get_key(self, key):
        self.key = key

    def get_children(self):
        return self.children

    def set_children(self, children):
        self.children = children

    def add_children(self, children):
        self.children.extend(children)
        return self


def construct():
    a = Tree('a')
    b = Tree('b')
    c = Tree('c')
    d = Tree('d')
    e = Tree('e')
    f = Tree('f')
    g = Tree('g')
    h = Tree('h')
    i = Tree('i')
    j = Tree('j')

    a.set_children([b, c, d])
    b.set_children([e, f, g])
    c.set_children([h])
    d.set_children([i, j])

    return a


def travel(node):
    if not node:
        return
    print(node.key, end=' ')
    for n in node.children:
        travel(n)


if __name__ == '__main__':
    tree = construct()
    travel(tree)
