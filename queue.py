# PRACA SKOŃCZONA

def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


class Queue:

    # konstruktor tworzacy pustą kolejke, o zadanej wartosci 5
    def __init__(self, size=5):
        self.size = size
        self.tab = [None for _ in range(self.size)]
        self.indeks_zap = 0
        self.indeks_od = 0

    def is_empty(self):
        if self.indeks_od == self.indeks_zap:
            return True

    def peek(self):
        if self.tab is not None:
            return self.tab[self.indeks_od]

    def dequeue(self):
        if self.indeks_od < self.size:
            if self.tab is not None:
                if self.indeks_od != self.size - 1:
                    self.indeks_od += 1
                    return self.tab[self.indeks_od-1]
        else:
            self.indeks_od = 0
            return self.tab[self.indeks_od]

    def enqueue(self, a: int):
        if self.indeks_zap == self.size:
            self.tab = realloc(self.tab, 2 * self.size)
            self.size = 2 * self.size
            self.tab[self.indeks_zap] = a
            self.indeks_zap += 1
        else:
            self.tab[self.indeks_zap] = a
            self.indeks_zap += 1

    def print_table(self):
        print(self.tab)

    def print_queue(self):
        for i in range(len(self.tab) - 1):
            while self.tab[self.indeks_od] is not None:
                print(self.tab[(self.indeks_od + i)])
                self.indeks_od += 1
        self.indeks_od = 0


# utowrzenie nowej kolejki
kolejka = Queue()
# wpisanie do kolejki liczb od 1 do 4:
kolejka.enqueue(1)
kolejka.enqueue(2)
kolejka.enqueue(3)
kolejka.enqueue(4)
print('uzycie dequeue do odczytu pierwszej danej i wypisane jej:')
print(kolejka.dequeue())
print('uzycie peek do odczytu drugiej danej i wypisanie jej:')
print(kolejka.peek())
print('testowe wypisanie kolejki: ')
kolejka.print_queue()
# dodanie liczb od 5 - 8 do tablicy
kolejka.enqueue(5)
kolejka.enqueue(6)
kolejka.enqueue(7)
kolejka.enqueue(8)
print('testowe wypisanie tablicy: ')
kolejka.print_table()
# print('testowe wypisanie tablicy:')
print('oprożnienie kolejki z wypisaniem danych:')
while not kolejka.is_empty():
    print(kolejka.dequeue())
print('wypisanie pustej kolejki: ')
kolejka.print_queue()

