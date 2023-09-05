# PRACA SKOŃCZONA
class Element:

    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __gt__(self, other):
        return self.priority > other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return self.priority + ":" + self.data


class HeapQueue:

    def __init__(self):
        self.tab = []

    def is_empty(self):
        if len(self.tab) == 0:
            return True

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.tab[0], self.tab[-1] = self.tab[-1], self.tab[0]
            temp = self.tab.pop()
            self.enqueue_(0)
            return temp.data

    def peek(self):
        return self.tab[0].data

    @staticmethod
    def parent(b):
        return int((b - 1) / 2)

    @staticmethod
    def left(c):
        return 2 * c + 1

    @staticmethod
    def right(d):
        return 2 * d + 2

    def enqueue_(self, i):
        while self.parent(i) < len(self.tab) and self.tab[i] > self.tab[self.parent(i)]:
            self.tab[i], self.tab[self.parent(i)] = self.tab[self.parent(i)], self.tab[i]
            i = self.parent(i)

    def enqueue(self, priority, data):
        elem = Element(priority, data)
        self.tab.append(elem)
        self.enqueue_(len(self.tab) - 1)

    def print_tab(self):
        if len(self.tab) == 0:
            print('{ }')
        else:
            print('{', end=' ')
            for i in range(len(self.tab) - 1):
                print(self.tab[i].priority, ':', self.tab[i].data, end=', ')
            if self.tab[len(self.tab) - 1]:
                print(self.tab[len(self.tab) - 1].priority, ':', self.tab[len(self.tab) - 1].data, end=' ')
            print('}')

    def print_tree(self, idx, lvl):
        if idx < len(self.tab):
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx].priority, ':', self.tab[idx].data if self.tab[idx].priority else None)
            self.print_tree(self.left(idx), lvl + 1)


stos = HeapQueue()
a = [4, 7, 6, 7, 5, 2, 2, 1]
b = ['A', 'L', 'G', 'O', 'R', 'Y', 'T', 'M']
for i, j in zip(a, b):
    stos.enqueue(i, j)
stos.print_tree(0, 0)
stos.print_tab()
print(stos.dequeue())
print(stos.peek())
stos.print_tab()
while not stos.is_empty():
    print(stos.dequeue())
stos.print_tab()
