# PRACA SKOŃCZONA
import random
import time


class Element:

    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __gt__(self, other):
        return self.priority > other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return str(self.priority) + ':' + str(self.data)

    def __repr__(self):
        return str(self.priority) + ': ' + str(self.data)


class HeapQueue:

    def __init__(self):
        self.tab = []
        self.size = 0
        self.to_sort = []

    def is_empty(self):
        if len(self.tab) == 0:
            return True

    def peek(self):
        return self.tab[0]

    @staticmethod
    def parent(b):
        return (b - 1) // 2

    @staticmethod
    def left(c):
        return 2 * c + 1

    @staticmethod
    def right(d):
        return 2 * d + 2

    def dequeue(self):
        if self.is_empty() is not True:
            root = self.peek()
            self.tab[0] = self.tab[-1]
            self.tab.pop()
            i = 0
            if self.right(i) >= len(self.tab):
                if self.right(i) == len(self.tab):
                    next_i = self.left(i)
                else:
                    next_i = None
            elif self.tab[self.left(i)] > self.tab[self.right(i)]:
                next_i = self.left(i)
            else:
                next_i = self.right(i)
            while next_i and self.tab[i] < self.tab[next_i]:
                self.tab[i], self.tab[next_i] = self.tab[next_i], self.tab[i]
                i = next_i
                if self.right(i) < len(self.tab):
                    if self.tab[self.left(i)] > self.tab[self.right(i)]:
                        next_i = self.left(i)
                    else:
                        next_i = self.right(i)
                elif self.right(i) == len(self.tab):
                    next_i = self.left(i)
            return root

    def enqueue_(self, i):
        while self.parent(i) < len(self.tab) and self.tab[i] > self.tab[self.parent(i)]:
            self.tab[i], self.tab[self.parent(i)] = self.tab[self.parent(i)], self.tab[i]

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

    def heapify(self, tab):
        if type(tab[0]) is tuple:
            for i in tab:
                self.enqueue(i[0], i[1])
        else:
            for i in tab:
                self.enqueue(None, i)

    def heapsort(self):
        tab = []
        for i in range(len(self.tab)):
            dequeued = self.dequeue()
            tab.insert(0, dequeued)
        return tab

    def swap(self, tab):
        if type(tab[0]) is tuple:
            for i in range(len(tab)):
                priority = tab[i][0]
                data = tab[i][1]
                elem = Element(priority, data)
                self.tab.append(elem)
            for i in range(1, len(tab)):
                elem = self.tab[i]
                j = i - 1
                while j >= 0 and elem < self.tab[j]:
                    self.tab[j + 1] = self.tab[j]
                    j -= 1
                self.tab[j + 1] = elem
        else:
            for i in range(1, len(tab)):
                elem = tab[i]
                j = i - 1
                while j >= 0 and elem < tab[j]:
                    tab[j + 1] = tab[j]
                    j -= 1
                tab[j + 1] = elem
            return tab

    def shift(self, tab):
        if type(tab[0]) is tuple:
            for i in range(len(tab)):
                priority = tab[i][0]
                data = tab[i][1]
                elem = Element(priority, data)
                self.tab.append(elem)
            for i in range(len(tab)):
                mini = i
                for j in range(i+1, len(tab)):
                    if self.tab[j] < self.tab[mini]:
                        mini = j
                if i != mini:
                    self.tab[i], self.tab[mini] = self.tab[mini], self.tab[i]
        else:
            for i in range(len(tab)):
                mini = i
                for j in range(i + 1, len(tab)):
                    if tab[j] < tab[mini]:
                        mini = j
                if i != mini:
                    tab[i], tab[mini] = tab[mini], tab[i]
        return tab


kopiec = HeapQueue()
tab = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
kopiec.heapify(tab)
kopiec.print_tree(0, 0)
print(kopiec.heapsort())
tab_2 = [(int(random.random() * 100), 'A') for i in range(10000)]
# dodałem losową daną 'A' dla lepszego wykorzystania kodu do pomiaru czasu
kopiec.heapify(tab_2)
t_start = time.perf_counter()
kopiec.heapsort()
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

# GOTOWE

# sortowanie przez zamiane
kopiec.swap(tab)
kopiec.print_tab()
# sortowanie przez wybieranie
kopiec_2 = HeapQueue()
kopiec_2.shift(tab)
kopiec_2.print_tab()

tab_3 = [int(random.random() * 100) for i in range(10000)]
t_start = time.perf_counter()
kopiec.swap(tab_3)
t_stop = time.perf_counter()
print(tab_3)
print("Czas obliczeń(swap):", "{:.7f}".format(t_stop - t_start))
t_start = time.perf_counter()
kopiec.shift(tab_3)
t_stop = time.perf_counter()
print(tab_3)
print("Czas obliczeń(shift):", "{:.7f}".format(t_stop - t_start))
