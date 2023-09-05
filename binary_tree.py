class RootNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.node_less = None
        self.node_more = None


def finding_min(node):
    temp = node
    while temp.node_less is not None:
        temp = temp.node_less
    return temp


class BSTree:

    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is not None:
            self.insert_2(self.root, key, data)
        else:
            self.root = RootNode(key, data)

    def insert_2(self, node, key, data):
        if node is None:
            return RootNode(key, data)
        if key > node.key:
            node.node_more = self.insert_2(node.node_more, key, data)
        if key < node.key:
            node.node_less = self.insert_2(node.node_less, key, data)
        else:
            node.value = data
        return node

    def search(self, node, key):
        if key < node.key:
            if node.node_less is not None:
                self.search(node.node_less, key)
            else:
                return None
        elif key > node.key:
            if node.node_more is not None:
                self.search(node.node_more, key)
            else:
                return None
        else:
            return node.value

    def delete(self, key):
        return self.delete_2(self.root, key)

    def delete_2(self, node, key):
        if key > node.key:
            node.node_more = self.delete_2(node.node_more, key)
        elif key < node.key:
            node.node_less = self.delete_2(node.node_less, key)
        else:
            if node.node_less is None:
                a = node.node_more
                return a
            elif node.node_more is None:
                a = node.node_less
                return a
            a = finding_min(node.node_more)
            node.key = a.key
            node.node_more = self.delete_2(node.node_more, a.key)
        return node

    def print_tree_as_table(self):
        if self.root is not None:
            self.print_tree_as_table_2(self.root)

    def print_tree_as_table_2(self, node):
        if node is not None:
            self.print_tree_as_table_2(node.node_less)
            print("{0}: {1}".format(node.key, node.value))
            self.print_tree_as_table_2(node.node_more)

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.node_more, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self._print_tree(node.node_less, lvl + 5)

    def height_2(self, node, key):
        if node is not None:
            node_more = self.height_2(node.node_more, key + 1)
            node_less = self.height_2(node.node_less, key + 1)
            return max(node_less, node_more)
        else:
            return key

    def height(self, node):
        if node is not None:
            return self.height_2(node, 0)
        else:
            return 0


drzewo = BSTree()
a = [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'K']

for i, j in zip(a, b):
    drzewo.insert(i, j)

drzewo.print_tree()
drzewo.print_tree_as_table()
print(drzewo.search(drzewo.root, 24))
drzewo.insert(20, 'AA')
drzewo.insert(6, 'M')
drzewo.delete(62)
drzewo.insert(59, 'N')
drzewo.insert(100, 'P')
drzewo.delete(8)
drzewo.delete(15)
drzewo.insert(55, 'R')
drzewo.delete(50)
drzewo.delete(5)
drzewo.delete(24)
print(drzewo.height(drzewo.root))
drzewo.print_tree_as_table()
drzewo.print_tree()

